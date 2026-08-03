"""
Unit tests for ThingsboardClient __getattr__ facade delegation.

Covers requirements FAC-01, FAC-02, FAC-05, FAC-06, FAC-07, FAC-08.

The tests import from tb_ce_client which is made importable via conftest.py
inserting ce/ into sys.path. Before importing ThingsboardClient, we ensure
that _controller_map.py exists in ce/tb_ce_client/.
"""

import sys
from pathlib import Path

import pytest

# ---------------------------------------------------------------------------
# Ensure _controller_map.py exists before any tb_ce_client imports
# ---------------------------------------------------------------------------

_REPO_ROOT = Path(__file__).parent.parent
_CE_PKG_DIR = _REPO_ROOT / "ce" / "tb_ce_client"
_CONTROLLER_MAP_PATH = _CE_PKG_DIR / "_controller_map.py"

# Generate the controller map if not present (idempotent — post_process already runs it)
if not _CONTROLLER_MAP_PATH.exists():
    _SCRIPTS_DIR = str(_REPO_ROOT / "scripts")
    if _SCRIPTS_DIR not in sys.path:
        sys.path.insert(0, _SCRIPTS_DIR)
    import post_process

    content, _mc, _cc = post_process._generate_controller_map(_CE_PKG_DIR / "api", "tb_ce_client")
    from post_process import LICENSE_HEADER

    _CONTROLLER_MAP_PATH.write_text(LICENSE_HEADER + content, encoding="utf-8")

# Ensure ce/ is in sys.path (conftest.py does this, but be defensive)
_CE_DIR = str(_REPO_ROOT / "ce")
if _CE_DIR not in sys.path:
    sys.path.insert(0, _CE_DIR)

# Do not overlay common/client.py onto the ce copy here: the committed copy is what
# users install, and repairing it at import time would defeat tests/test_common_overlay.py.

# Evict any stale tb_ce_client imports so the committed client.py is picked up
for mod_name in list(sys.modules.keys()):
    if mod_name == "tb_ce_client" or mod_name.startswith("tb_ce_client."):
        del sys.modules[mod_name]

from tb_ce_client._controller_map import _CONTROLLER_ATTR_MAP, _CONTROLLER_MAP
from tb_ce_client.client import ThingsboardClient

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _make_client() -> ThingsboardClient:
    """Construct a ThingsboardClient with api_key (no network calls)."""
    return ThingsboardClient("http://localhost:9090", api_key="test-key", retry_on_rate_limit=False)


# ---------------------------------------------------------------------------
# FAC-01 / FAC-02: Facade delegation
# ---------------------------------------------------------------------------


class TestFacadeDelegation:
    """FAC-01: __getattr__ delegates method calls to the correct controller.
    FAC-02: All methods in _CONTROLLER_MAP are accessible on a ThingsboardClient instance.
    """

    def test_get_tenant_devices_callable(self):
        """client.get_tenant_devices resolves to a bound method (FAC-01)."""
        client = _make_client()
        method = client.get_tenant_devices
        assert callable(method), "get_tenant_devices should be callable"

    def test_method_bound_to_device_controller(self):
        """client.get_tenant_devices is bound to a DeviceControllerApi instance."""
        from tb_ce_client.api.device_controller_api import DeviceControllerApi

        client = _make_client()
        method = client.get_tenant_devices
        # The bound method's __self__ should be a DeviceControllerApi
        assert isinstance(method.__self__, DeviceControllerApi), (
            f"Expected DeviceControllerApi, got {type(method.__self__)}"
        )

    def test_sampling_of_methods_from_different_controllers(self):
        """A sampling of methods from different controllers are all accessible (FAC-02)."""
        client = _make_client()
        sample_methods = [
            "get_tenant_devices",  # DeviceControllerApi
            "get_alarm_by_id",  # AlarmControllerApi
            "get_customers",  # CustomerControllerApi
            "delete_dashboard",  # DashboardControllerApi
            "find_assets_by_query",  # AssetControllerApi
        ]
        for method_name in sample_methods:
            method = getattr(client, method_name)
            assert callable(method), f"{method_name} should be callable on ThingsboardClient"

    def test_all_controller_map_methods_accessible(self):
        """Every method in _CONTROLLER_MAP can be resolved on client (FAC-02)."""
        client = _make_client()
        failures = []
        for method_name in _CONTROLLER_MAP:
            try:
                method = getattr(client, method_name)
                if not callable(method):
                    failures.append(f"{method_name}: not callable")
            except AttributeError as e:
                failures.append(f"{method_name}: {e}")
        assert not failures, f"{len(failures)} methods inaccessible: {failures[:5]}"


# ---------------------------------------------------------------------------
# FAC-05: Direct controller import
# ---------------------------------------------------------------------------


class TestDirectImport:
    """FAC-05: from tb_ce_client.api.device_controller_api import DeviceControllerApi works."""

    def test_direct_import_device_controller(self):
        """Direct import of DeviceControllerApi from its module succeeds."""
        from tb_ce_client.api.device_controller_api import DeviceControllerApi

        assert DeviceControllerApi is not None

    def test_direct_import_can_instantiate(self):
        """DeviceControllerApi can be instantiated with an ApiClient."""
        from tb_ce_client.api.device_controller_api import DeviceControllerApi

        client = _make_client()
        api = DeviceControllerApi(client.api_client)
        assert isinstance(api, DeviceControllerApi)


# ---------------------------------------------------------------------------
# FAC-06: Auth routing — login maps to LoginEndpointApi
# ---------------------------------------------------------------------------


class TestAuthRouting:
    """FAC-06: client.login resolves to LoginEndpointApi.login."""

    def test_login_in_controller_map(self):
        """_CONTROLLER_MAP contains 'login' key."""
        assert "login" in _CONTROLLER_MAP, "'login' must be in _CONTROLLER_MAP"

    def test_login_maps_to_login_endpoint_api(self):
        """_CONTROLLER_MAP['login'] maps to LoginEndpointApi (not AuthControllerApi)."""
        module_path, cls_name = _CONTROLLER_MAP["login"]
        assert cls_name == "LoginEndpointApi", f"Expected LoginEndpointApi, got {cls_name}"
        assert "login_endpoint_api" in module_path

    def test_client_login_bound_to_login_endpoint_api(self):
        """client.login is bound to a LoginEndpointApi instance."""
        from tb_ce_client.api.login_endpoint_api import LoginEndpointApi

        client = _make_client()
        method = client.login
        assert callable(method)
        assert isinstance(method.__self__, LoginEndpointApi), (
            f"Expected LoginEndpointApi, got {type(method.__self__)}"
        )


# ---------------------------------------------------------------------------
# FAC-07: Lazy instantiation and caching
# ---------------------------------------------------------------------------


class TestLazyInstantiation:
    """FAC-07: Controller instances are cached; all share the same api_client."""

    def test_controller_cached_on_repeated_access(self):
        """Accessing the same method twice returns the same controller instance."""
        client = _make_client()
        _ = client.get_tenant_devices  # first access
        _ = client.get_tenant_devices  # second access
        # Both should come from the same cached controller
        from tb_ce_client.api.device_controller_api import DeviceControllerApi

        module_path, cls_name = _CONTROLLER_MAP["get_tenant_devices"]
        cached = client._controllers[cls_name]
        assert isinstance(cached, DeviceControllerApi)
        # Ensure accessing again returns same object
        method2 = client.get_tenant_devices
        assert method2.__self__ is cached, "Controller should be the same cached instance"

    def test_controller_shares_api_client(self):
        """All controller instances share the same ApiClient as the ThingsboardClient."""
        client = _make_client()
        _ = client.get_tenant_devices
        _ = client.get_alarm_by_id
        _ = client.find_assets_by_query

        for cls_name, ctrl_instance in client._controllers.items():
            assert ctrl_instance.api_client is client.api_client, (
                f"{cls_name}.api_client is not the same object as client.api_client"
            )


# ---------------------------------------------------------------------------
# FAC-08: Named controller attributes
# ---------------------------------------------------------------------------


class TestNamedControllerAttrs:
    """FAC-08: client.device_controller and client.asset_controller return correct types."""

    def test_device_controller_attr(self):
        """client.device_controller returns a DeviceControllerApi instance."""
        from tb_ce_client.api.device_controller_api import DeviceControllerApi

        client = _make_client()
        ctrl = client.device_controller
        assert isinstance(ctrl, DeviceControllerApi), (
            f"Expected DeviceControllerApi, got {type(ctrl)}"
        )

    def test_asset_controller_attr(self):
        """client.asset_controller returns an AssetControllerApi instance."""
        from tb_ce_client.api.asset_controller_api import AssetControllerApi

        client = _make_client()
        ctrl = client.asset_controller
        assert isinstance(ctrl, AssetControllerApi), (
            f"Expected AssetControllerApi, got {type(ctrl)}"
        )

    def test_named_controller_in_attr_map(self):
        """All short names in _CONTROLLER_ATTR_MAP are accessible on client."""
        client = _make_client()
        failures = []
        for short_name in _CONTROLLER_ATTR_MAP:
            try:
                ctrl = getattr(client, short_name)
                if ctrl is None:
                    failures.append(f"{short_name}: returned None")
            except AttributeError as e:
                failures.append(f"{short_name}: {e}")
        assert not failures, f"{len(failures)} controller attrs inaccessible: {failures[:5]}"


# ---------------------------------------------------------------------------
# Edge cases
# ---------------------------------------------------------------------------


class TestGetAttrEdgeCases:
    """Error handling and recursion guard."""

    def test_attribute_error_for_nonexistent(self):
        """client.nonexistent_method raises AttributeError."""
        client = _make_client()
        with pytest.raises(AttributeError):
            _ = client.nonexistent_method_xyz_abc

    def test_attribute_error_message_includes_name(self):
        """AttributeError message contains the attribute name."""
        client = _make_client()
        with pytest.raises(AttributeError, match="nonexistent_xyz"):
            _ = client.nonexistent_xyz

    def test_getattr_guard_prevents_recursion(self):
        """__getattr__ returns AttributeError immediately if _controllers not in __dict__."""
        client = _make_client()
        # Manually delete _controllers to simulate partial-init state
        del client.__dict__["_controllers"]
        with pytest.raises(AttributeError):
            _ = client.some_method


# ---------------------------------------------------------------------------
# FAC-04: Type stubs (.pyi validation)
# ---------------------------------------------------------------------------


class TestTypeStub:
    """FAC-04: client.pyi provides IDE autocompletion and mypy compatibility."""

    _PYI_PATH = _REPO_ROOT / "ce" / "tb_ce_client" / "client.pyi"

    def test_client_pyi_exists(self):
        """ce/tb_ce_client/client.pyi exists after generation."""
        assert self._PYI_PATH.exists(), (
            f"client.pyi not found at {self._PYI_PATH}. "
            "Run: python3 scripts/post_process.py ce/tb_ce_client tb_ce_client"
        )

    def test_client_pyi_has_method_stubs(self):
        """client.pyi contains def get_device_by_id method stub."""
        content = self._PYI_PATH.read_text(encoding="utf-8")
        assert "def get_device_by_id" in content, "Expected 'def get_device_by_id' in client.pyi"

    def test_client_pyi_has_controller_properties(self):
        """client.pyi contains @property and def device_controller."""
        content = self._PYI_PATH.read_text(encoding="utf-8")
        assert "@property" in content, "Expected '@property' in client.pyi"
        assert "def device_controller" in content, (
            "Expected 'def device_controller' property in client.pyi"
        )

    def test_client_pyi_is_valid_python(self):
        """client.pyi compiles as valid Python (no syntax errors)."""
        content = self._PYI_PATH.read_text(encoding="utf-8")
        try:
            compile(content, "client.pyi", "exec")
        except SyntaxError as e:
            pytest.fail(f"client.pyi has syntax error: {e}")

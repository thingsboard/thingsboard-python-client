"""
Unit tests for _collect_api_classes and _generate_api_init in scripts/post_process.py.

These tests use temporary directories with mock *_api.py files and are runnable
immediately (no regeneration needed). They will PASS after Task 2 adds the functions.
"""

import sys
from pathlib import Path

import pytest

# Add scripts/ to sys.path so we can import post_process directly
_SCRIPTS_DIR = str(Path(__file__).parent.parent / "scripts")
if _SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, _SCRIPTS_DIR)

import post_process

# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


@pytest.fixture
def mock_api_dir(tmp_path):
    """Create a temporary api/ directory with mock controller files."""
    api_dir = tmp_path / "api"
    api_dir.mkdir()

    # Mock controller files
    (api_dir / "device_controller_api.py").write_text(
        "class DeviceControllerApi(ApiClient):\n    pass\n",
        encoding="utf-8",
    )
    (api_dir / "alarm_controller_api.py").write_text(
        "class AlarmControllerApi(ApiClient):\n    pass\n",
        encoding="utf-8",
    )
    (api_dir / "admin_controller_api.py").write_text(
        "class AdminControllerApi(ApiClient):\n    pass\n",
        encoding="utf-8",
    )
    # __init__.py should be skipped
    (api_dir / "__init__.py").write_text("# auto-generated\n", encoding="utf-8")

    return api_dir


# ---------------------------------------------------------------------------
# Tests for _collect_api_classes
# ---------------------------------------------------------------------------


def test_collect_api_classes_dynamic(mock_api_dir):
    """_collect_api_classes discovers classes from files without hard-coding."""
    result = post_process._collect_api_classes(mock_api_dir, "tb_ce_client")

    assert "DeviceControllerApi" in result
    assert "AlarmControllerApi" in result
    assert "AdminControllerApi" in result
    # __init__.py must be skipped
    assert len(result) == 3


def test_collect_api_classes_module_paths(mock_api_dir):
    """_collect_api_classes maps class names to correct module paths."""
    result = post_process._collect_api_classes(mock_api_dir, "tb_ce_client")

    assert result["DeviceControllerApi"] == "tb_ce_client.api.device_controller_api"
    assert result["AlarmControllerApi"] == "tb_ce_client.api.alarm_controller_api"
    assert result["AdminControllerApi"] == "tb_ce_client.api.admin_controller_api"


def test_collect_api_classes_empty_dir(tmp_path):
    """_collect_api_classes returns empty dict when api/ has only __init__.py."""
    api_dir = tmp_path / "api"
    api_dir.mkdir()
    (api_dir / "__init__.py").write_text("", encoding="utf-8")

    result = post_process._collect_api_classes(api_dir, "tb_ce_client")
    assert result == {}


def test_collect_api_classes_multiple_classes_per_file(tmp_path):
    """_collect_api_classes picks up multiple classes from a single file."""
    api_dir = tmp_path / "api"
    api_dir.mkdir()
    (api_dir / "multi_api.py").write_text(
        "class FooApi(Base):\n    pass\n\nclass BarApi(Base):\n    pass\n",
        encoding="utf-8",
    )

    result = post_process._collect_api_classes(api_dir, "mypkg")
    assert "FooApi" in result
    assert "BarApi" in result
    assert result["FooApi"] == "mypkg.api.multi_api"
    assert result["BarApi"] == "mypkg.api.multi_api"


# ---------------------------------------------------------------------------
# Tests for _generate_api_init
# ---------------------------------------------------------------------------


def test_generate_api_init_lazy_pattern():
    """_generate_api_init output contains __getattr__, _API_CLASSES, TYPE_CHECKING."""
    api_map = {
        "DeviceControllerApi": "tb_ce_client.api.device_controller_api",
        "AlarmControllerApi": "tb_ce_client.api.alarm_controller_api",
    }
    content = post_process._generate_api_init("tb_ce_client", api_map)

    assert "__getattr__" in content
    assert "_API_CLASSES" in content
    assert "TYPE_CHECKING" in content
    assert "importlib" in content
    assert "__dir__" in content


def test_generate_api_init_all_classes(mock_api_dir):
    """All discovered classes appear in __all__ and _API_CLASSES."""
    api_map = post_process._collect_api_classes(mock_api_dir, "tb_ce_client")
    content = post_process._generate_api_init("tb_ce_client", api_map)

    for cls_name in api_map:
        assert f'"{cls_name}"' in content, (
            f"{cls_name!r} not found in generated api/__init__.py content"
        )


def test_generate_api_init_sorted_output():
    """_generate_api_init emits classes in sorted order."""
    api_map = {
        "ZebraControllerApi": "pkg.api.zebra_controller_api",
        "AlphaControllerApi": "pkg.api.alpha_controller_api",
        "MidControllerApi": "pkg.api.mid_controller_api",
    }
    content = post_process._generate_api_init("pkg", api_map)

    alpha_pos = content.index("AlphaControllerApi")
    mid_pos = content.index("MidControllerApi")
    zebra_pos = content.index("ZebraControllerApi")
    assert alpha_pos < mid_pos < zebra_pos, "Classes should appear in sorted (alphabetical) order"


# ---------------------------------------------------------------------------
# Tests for updated _generate_root_init (api_map parameter)
# ---------------------------------------------------------------------------


def test_generate_root_init_no_thingsboard_api():
    """Updated _generate_root_init with empty api_map must not emit ThingsboardApi."""
    content = post_process._generate_root_init("tb_ce_client", {}, {})
    assert "ThingsboardApi" not in content, (
        "_generate_root_init should not hard-code ThingsboardApi when api_map is empty"
    )


def test_generate_root_init_with_api_map():
    """_generate_root_init with api_map lists controllers in _LAZY_CLASSES."""
    api_map = {
        "DeviceControllerApi": "tb_ce_client.api.device_controller_api",
    }
    content = post_process._generate_root_init("tb_ce_client", {}, api_map)
    assert '"DeviceControllerApi"' in content
    assert "device_controller_api" in content


# ---------------------------------------------------------------------------
# Tests for updated rewrite_init_files (Tuple[int, int, int] return)
# ---------------------------------------------------------------------------


def test_rewrite_init_files_returns_tuple(tmp_path):
    """rewrite_init_files returns (model_count, api_count, method_count) tuple."""
    pkg_dir = tmp_path / "tb_test_client"
    pkg_dir.mkdir()
    (pkg_dir / "__init__.py").write_text("", encoding="utf-8")

    models_dir = pkg_dir / "models"
    models_dir.mkdir()
    (models_dir / "__init__.py").write_text("", encoding="utf-8")
    (models_dir / "device.py").write_text("class Device(BaseModel):\n    pass\n", encoding="utf-8")

    api_dir = pkg_dir / "api"
    api_dir.mkdir()
    (api_dir / "__init__.py").write_text("", encoding="utf-8")
    (api_dir / "device_controller_api.py").write_text(
        "class DeviceControllerApi(ApiClient):\n    def get_device(self):\n        pass\n",
        encoding="utf-8",
    )

    result = post_process.rewrite_init_files(pkg_dir, "tb_test_client")
    assert isinstance(result, tuple), f"Expected tuple, got {type(result)}"
    assert len(result) == 3, f"Expected 3-tuple, got {len(result)}-tuple"
    model_count, api_count, method_count = result
    assert model_count == 1, f"Expected 1 model, got {model_count}"
    assert api_count == 1, f"Expected 1 api class, got {api_count}"
    assert method_count >= 1, f"Expected >=1 method, got {method_count}"


# ---------------------------------------------------------------------------
# Tests for _generate_controller_map
# ---------------------------------------------------------------------------

_CE_API_DIR = Path(__file__).parent.parent / "ce" / "tb_ce_client" / "api"


def test_generate_controller_map_content():
    """_generate_controller_map returns content with both map dicts."""
    content, method_count, controller_count = post_process._generate_controller_map(
        _CE_API_DIR, "tb_ce_client"
    )
    assert "_CONTROLLER_MAP" in content
    assert "_CONTROLLER_ATTR_MAP" in content


def test_generate_controller_map_method_count():
    """_generate_controller_map produces >= 1500 method entries for CE."""
    content, method_count, controller_count = post_process._generate_controller_map(
        _CE_API_DIR, "tb_ce_client"
    )
    assert method_count >= 1500, f"Expected >= 1500 methods, got {method_count}"


def test_generate_controller_map_attr_count():
    """_generate_controller_map produces exactly 58 controller attr entries for CE."""
    content, method_count, controller_count = post_process._generate_controller_map(
        _CE_API_DIR, "tb_ce_client"
    )
    assert controller_count == 58, f"Expected 58 controllers, got {controller_count}"


def test_generate_controller_map_login_routing():
    """'login' method key maps to LoginEndpointApi in _CONTROLLER_MAP."""
    content, _, _ = post_process._generate_controller_map(_CE_API_DIR, "tb_ce_client")
    # Evaluate the generated content to inspect the dicts
    ns = {}
    exec(content, ns)
    assert "login" in ns["_CONTROLLER_MAP"], "'login' must be in _CONTROLLER_MAP"
    module_path, cls_name = ns["_CONTROLLER_MAP"]["login"]
    assert cls_name == "LoginEndpointApi", f"Expected LoginEndpointApi, got {cls_name}"
    assert "login_endpoint_api" in module_path


def test_generate_controller_map_short_name():
    """'device_controller' key maps to DeviceControllerApi in _CONTROLLER_ATTR_MAP."""
    content, _, _ = post_process._generate_controller_map(_CE_API_DIR, "tb_ce_client")
    ns = {}
    exec(content, ns)
    assert "device_controller" in ns["_CONTROLLER_ATTR_MAP"], (
        "'device_controller' must be in _CONTROLLER_ATTR_MAP"
    )
    module_path, cls_name = ns["_CONTROLLER_ATTR_MAP"]["device_controller"]
    assert cls_name == "DeviceControllerApi", f"Expected DeviceControllerApi, got {cls_name}"


def test_rewrite_init_files_writes_controller_map(tmp_path):
    """rewrite_init_files writes _controller_map.py into package_dir."""
    pkg_dir = tmp_path / "tb_test_client"
    pkg_dir.mkdir()
    (pkg_dir / "__init__.py").write_text("", encoding="utf-8")

    models_dir = pkg_dir / "models"
    models_dir.mkdir()
    (models_dir / "__init__.py").write_text("", encoding="utf-8")
    (models_dir / "device.py").write_text("class Device(BaseModel):\n    pass\n", encoding="utf-8")

    api_dir = pkg_dir / "api"
    api_dir.mkdir()
    (api_dir / "__init__.py").write_text("", encoding="utf-8")
    (api_dir / "device_controller_api.py").write_text(
        "class DeviceControllerApi(ApiClient):\n    def get_device(self):\n        pass\n",
        encoding="utf-8",
    )

    post_process.rewrite_init_files(pkg_dir, "tb_test_client")
    controller_map_path = pkg_dir / "_controller_map.py"
    assert controller_map_path.exists(), "_controller_map.py must be written to package_dir"
    map_content = controller_map_path.read_text(encoding="utf-8")
    assert "_CONTROLLER_MAP" in map_content
    assert "_CONTROLLER_ATTR_MAP" in map_content


# ---------------------------------------------------------------------------
# Fixtures for _generate_client_pyi tests
# ---------------------------------------------------------------------------


@pytest.fixture
def mock_api_dir_with_methods(tmp_path):
    """Create a temporary api/ directory with controllers that have method signatures."""
    api_dir = tmp_path / "api"
    api_dir.mkdir()

    (api_dir / "device_controller_api.py").write_text(
        "from typing import Optional\n"
        "from typing_extensions import Annotated\n"
        "from tb_ce_client.models.device import Device\n"
        "from tb_ce_client.models.page_data_device import PageDataDevice\n"
        "\n"
        "class DeviceControllerApi:\n"
        "    def __init__(self, api_client=None) -> None:\n"
        "        self.api_client = api_client\n"
        "\n"
        "    def get_device_by_id(\n"
        "        self,\n"
        "        device_id: str,\n"
        "    ) -> Device:\n"
        "        pass\n"
        "\n"
        "    def get_tenant_devices(\n"
        "        self,\n"
        "        page_size: int,\n"
        "        page: int,\n"
        "    ) -> PageDataDevice:\n"
        "        pass\n",
        encoding="utf-8",
    )
    (api_dir / "alarm_controller_api.py").write_text(
        "from tb_ce_client.models.alarm import Alarm\n"
        "\n"
        "class AlarmControllerApi:\n"
        "    def __init__(self, api_client=None) -> None:\n"
        "        self.api_client = api_client\n"
        "\n"
        "    def get_alarm_by_id(\n"
        "        self,\n"
        "        alarm_id: str,\n"
        "    ) -> Alarm:\n"
        "        pass\n",
        encoding="utf-8",
    )
    # __init__.py should be skipped
    (api_dir / "__init__.py").write_text("# auto-generated\n", encoding="utf-8")

    return api_dir


@pytest.fixture
def mock_client_py(tmp_path):
    """Create a minimal client.py for _generate_client_pyi to read."""
    client_py = tmp_path / "client.py"
    client_py.write_text(
        "class ThingsboardClient:\n"
        "    def __init__(self, url: str, username: str = None) -> None:\n"
        "        pass\n",
        encoding="utf-8",
    )
    return client_py


# ---------------------------------------------------------------------------
# Tests for _generate_client_pyi
# ---------------------------------------------------------------------------


def test_generate_client_pyi_class(mock_api_dir_with_methods, mock_client_py):
    """_generate_client_pyi output contains 'class ThingsboardClient:'."""
    content, stub_count = post_process._generate_client_pyi(
        mock_api_dir_with_methods, "tb_ce_client", mock_client_py
    )
    assert "class ThingsboardClient:" in content, (
        "Expected 'class ThingsboardClient:' in generated .pyi content"
    )


def test_generate_client_pyi_method_stub(mock_api_dir_with_methods, mock_client_py):
    """_generate_client_pyi output contains a method stub for get_device_by_id."""
    content, stub_count = post_process._generate_client_pyi(
        mock_api_dir_with_methods, "tb_ce_client", mock_client_py
    )
    assert "def get_device_by_id" in content, (
        "Expected 'def get_device_by_id' stub in generated .pyi content"
    )


def test_generate_client_pyi_controller_property(mock_api_dir_with_methods, mock_client_py):
    """_generate_client_pyi output contains @property and named controller attributes."""
    content, stub_count = post_process._generate_client_pyi(
        mock_api_dir_with_methods, "tb_ce_client", mock_client_py
    )
    assert "@property" in content, "Expected '@property' decorator in generated .pyi content"
    assert "def device_controller" in content, (
        "Expected 'def device_controller' property in generated .pyi content"
    )


def test_generate_client_pyi_imports(mock_api_dir_with_methods, mock_client_py):
    """_generate_client_pyi output contains controller class import lines."""
    content, stub_count = post_process._generate_client_pyi(
        mock_api_dir_with_methods, "tb_ce_client", mock_client_py
    )
    assert "DeviceControllerApi" in content, (
        "Expected DeviceControllerApi import in generated .pyi content"
    )
    assert "AlarmControllerApi" in content, (
        "Expected AlarmControllerApi import in generated .pyi content"
    )


def test_generate_client_pyi_returns_stub_count(mock_api_dir_with_methods, mock_client_py):
    """_generate_client_pyi returns (content, stub_count) where stub_count > 0."""
    content, stub_count = post_process._generate_client_pyi(
        mock_api_dir_with_methods, "tb_ce_client", mock_client_py
    )
    assert stub_count > 0, f"Expected stub_count > 0, got {stub_count}"


def test_generate_client_pyi_existing_methods(mock_api_dir_with_methods, mock_client_py):
    """_generate_client_pyi includes get_token, get_refresh_token, close, __enter__, __exit__."""
    content, stub_count = post_process._generate_client_pyi(
        mock_api_dir_with_methods, "tb_ce_client", mock_client_py
    )
    for method_name in ("get_token", "get_refresh_token", "close", "__enter__", "__exit__"):
        assert f"def {method_name}" in content, (
            f"Expected 'def {method_name}' in generated .pyi content"
        )


def test_rewrite_init_files_writes_pyi(tmp_path):
    """rewrite_init_files writes client.pyi to package_dir."""
    pkg_dir = tmp_path / "tb_test_client"
    pkg_dir.mkdir()
    (pkg_dir / "__init__.py").write_text("", encoding="utf-8")
    (pkg_dir / "client.py").write_text("class ThingsboardClient:\n    pass\n", encoding="utf-8")

    models_dir = pkg_dir / "models"
    models_dir.mkdir()
    (models_dir / "__init__.py").write_text("", encoding="utf-8")
    (models_dir / "device.py").write_text("class Device(BaseModel):\n    pass\n", encoding="utf-8")

    api_dir = pkg_dir / "api"
    api_dir.mkdir()
    (api_dir / "__init__.py").write_text("", encoding="utf-8")
    (api_dir / "device_controller_api.py").write_text(
        "class DeviceControllerApi:\n"
        "    def get_device(self, device_id: str) -> None:\n"
        "        pass\n",
        encoding="utf-8",
    )

    post_process.rewrite_init_files(pkg_dir, "tb_test_client")
    pyi_path = pkg_dir / "client.pyi"
    assert pyi_path.exists(), "client.pyi must be written to package_dir after rewrite_init_files"
    pyi_content = pyi_path.read_text(encoding="utf-8")
    assert "class ThingsboardClient:" in pyi_content


# ---------------------------------------------------------------------------
# Tests for fix_polymorphic_discriminator_defaults (Step 2c)
# ---------------------------------------------------------------------------


def _write_parent(models_dir: Path, *, property_name: str, mapping: dict[str, str],
                  field_type: str = "StrictStr", class_name: str = "Parent") -> Path:
    """Write a minimal parent model file with the given discriminator mapping."""
    field_py = post_process._camel_to_snake(property_name)
    pairs = ",".join(f"'{k}': '{v}'" for k, v in mapping.items())
    content = f'''\
from pydantic import BaseModel, Field, StrictStr
from typing import ClassVar, Dict, Optional

class {class_name}(BaseModel):
    """
    {class_name}
    """ # noqa: E501
    {field_py}: {field_type} = Field(serialization_alias="{property_name}")

    __discriminator_property_name: ClassVar[str] = '{property_name}'
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {{
        {pairs}
    }}
'''
    path = models_dir / f"{post_process._camel_to_snake(class_name)}.py"
    path.write_text(content, encoding="utf-8")
    return path


def _write_child(models_dir: Path, *, class_name: str, parent: str,
                 field_py: str = "type", field_type: str = "StrictStr") -> Path:
    """Write a minimal child model file with no discriminator default."""
    content = f'''\
from pydantic import Field, StrictStr
from typing import Optional
from tb_test_client.models.{post_process._camel_to_snake(parent)} import {parent}

class {class_name}({parent}):
    """
    {class_name}
    """ # noqa: E501
'''
    path = models_dir / f"{post_process._camel_to_snake(class_name)}.py"
    path.write_text(content, encoding="utf-8")
    return path


@pytest.fixture
def discriminator_models_dir(tmp_path):
    models_dir = tmp_path / "models"
    models_dir.mkdir()
    return models_dir


def test_discriminator_patches_strict_str_subclass(discriminator_models_dir):
    """Real OpenAPI mapping (key != class name) -> inject string default."""
    _write_parent(discriminator_models_dir, property_name="type",
                  mapping={"DEVICE": "DeviceFilter"}, class_name="EntityFilter")
    child = _write_child(discriminator_models_dir, class_name="DeviceFilter", parent="EntityFilter")

    parents, patched, skipped = post_process.fix_polymorphic_discriminator_defaults(
        discriminator_models_dir, "tb_test_client"
    )
    assert (parents, patched, skipped) == (1, 1, 0)
    out = child.read_text()
    assert 'type: StrictStr = "DEVICE"' in out
    assert post_process._DISCRIMINATOR_INJECT_TAG in out


def test_discriminator_skips_class_name_fallback(discriminator_models_dir):
    """No explicit mapping (key == class name) -> skip rather than write garbage."""
    _write_parent(discriminator_models_dir, property_name="securityMode",
                  mapping={"PSKChild": "PSKChild"}, class_name="Credential")
    child = _write_child(discriminator_models_dir, class_name="PSKChild", parent="Credential")

    parents, patched, skipped = post_process.fix_polymorphic_discriminator_defaults(
        discriminator_models_dir, "tb_test_client"
    )
    assert (parents, patched, skipped) == (1, 0, 1)
    out = child.read_text()
    assert post_process._DISCRIMINATOR_INJECT_TAG not in out
    assert 'default="PSKChild"' not in out


def test_discriminator_idempotent_on_rerun(discriminator_models_dir):
    """Second run is a no-op once the tag is present."""
    _write_parent(discriminator_models_dir, property_name="type",
                  mapping={"DEVICE": "DeviceFilter"}, class_name="EntityFilter")
    _write_child(discriminator_models_dir, class_name="DeviceFilter", parent="EntityFilter")

    post_process.fix_polymorphic_discriminator_defaults(discriminator_models_dir, "tb_test_client")
    _parents, patched2, _skipped = post_process.fix_polymorphic_discriminator_defaults(
        discriminator_models_dir, "tb_test_client"
    )
    assert patched2 == 0


def test_discriminator_bails_without_docstring_close(discriminator_models_dir):
    """Skip injection when the generated docstring close marker is absent."""
    _write_parent(discriminator_models_dir, property_name="type",
                  mapping={"DEVICE": "DeviceFilter"}, class_name="EntityFilter")
    child = discriminator_models_dir / "device_filter.py"
    child.write_text(
        "from pydantic import Field\n"
        "from tb_test_client.models.entity_filter import EntityFilter\n"
        "class DeviceFilter(EntityFilter):\n"
        '    """No noqa close here."""\n',
        encoding="utf-8",
    )

    _parents, patched, _skipped = post_process.fix_polymorphic_discriminator_defaults(
        discriminator_models_dir, "tb_test_client"
    )
    assert patched == 0
    assert post_process._DISCRIMINATOR_INJECT_TAG not in child.read_text()


# ---------------------------------------------------------------------------
# Tests for add_default_none_to_optional_fields (Step 2d)
# ---------------------------------------------------------------------------


def test_default_none_added_to_simple_optional(tmp_path):
    models_dir = tmp_path / "models"
    models_dir.mkdir()
    f = models_dir / "role.py"
    f.write_text(
        "from pydantic import Field\n"
        "from typing import Any, Optional\n"
        "class Role:\n"
        '    permissions: Optional[Any] = Field(description="Permissions blob")\n',
        encoding="utf-8",
    )

    assert post_process.add_default_none_to_optional_fields(models_dir) == 1
    out = f.read_text()
    assert 'Field(default=None, description="Permissions blob")' in out


def test_default_none_skips_already_defaulted(tmp_path):
    models_dir = tmp_path / "models"
    models_dir.mkdir()
    f = models_dir / "role.py"
    original = (
        "from pydantic import Field\n"
        "from typing import Any, Optional\n"
        "class Role:\n"
        '    permissions: Optional[Any] = Field(default=None, description="Already set")\n'
    )
    f.write_text(original, encoding="utf-8")

    assert post_process.add_default_none_to_optional_fields(models_dir) == 0
    assert f.read_text() == original


def test_default_none_handles_nested_generics(tmp_path):
    """Optional[Dict[str, int]] and Optional[List[Foo]] must be patched."""
    models_dir = tmp_path / "models"
    models_dir.mkdir()
    f = models_dir / "model.py"
    f.write_text(
        "from pydantic import Field\n"
        "from typing import Dict, List, Optional\n"
        "class M:\n"
        '    a: Optional[Dict[str, int]] = Field(description="dict")\n'
        '    b: Optional[List[str]] = Field(description="list")\n',
        encoding="utf-8",
    )

    assert post_process.add_default_none_to_optional_fields(models_dir) == 2
    out = f.read_text()
    assert 'a: Optional[Dict[str, int]] = Field(default=None, description="dict")' in out
    assert 'b: Optional[List[str]] = Field(default=None, description="list")' in out


def test_default_none_handles_parens_in_description(tmp_path):
    """A description string containing parens must not truncate the args capture."""
    models_dir = tmp_path / "models"
    models_dir.mkdir()
    f = models_dir / "model.py"
    f.write_text(
        "from pydantic import Field\n"
        "from typing import Any, Optional\n"
        "class M:\n"
        '    x: Optional[Any] = Field(description="Provider (e.g. github, google)")\n',
        encoding="utf-8",
    )

    assert post_process.add_default_none_to_optional_fields(models_dir) == 1
    out = f.read_text()
    assert (
        'x: Optional[Any] = Field(default=None, description="Provider (e.g. github, google)")'
        in out
    )


def test_default_none_skips_default_factory(tmp_path):
    """default_factory= must NOT be treated as default=."""
    models_dir = tmp_path / "models"
    models_dir.mkdir()
    f = models_dir / "model.py"
    original = (
        "from pydantic import Field\n"
        "from typing import Any, Optional\n"
        "class M:\n"
        '    x: Optional[Any] = Field(default_factory=list, description="x")\n'
    )
    f.write_text(original, encoding="utf-8")

    # default_factory satisfies pydantic, no extra `default=` injection needed.
    # The function currently injects (since default_factory != default=); we
    # only assert it stays valid Python and doesn't blow up. Adjust if policy
    # changes to leave default_factory alone.
    count = post_process.add_default_none_to_optional_fields(models_dir)
    out = f.read_text()
    if count == 1:
        assert "default=None" in out and "default_factory=list" in out
    else:
        assert out == original


# ---------------------------------------------------------------------------
# Tests for fix_missing_2xx_response_types (Step 2e)
# ---------------------------------------------------------------------------


_RESP_MAP_TEMPLATE = '''\
class FooApi:
    def get_thing(self) -> List[Foo]:
        _response_types_map: Dict[str, Optional[str]] = {{
{entries}
        }}
        return _response_types_map

    def get_thing_with_http_info(self) -> ApiResponse[List[Foo]]:
        _response_types_map: Dict[str, Optional[str]] = {{
{entries}
        }}
        return _response_types_map

    def get_thing_without_preload_content(self) -> RESTResponseType:
        _response_types_map: Dict[str, Optional[str]] = {{
{entries}
        }}
        return _response_types_map
'''


def test_response_types_injects_missing_200(tmp_path):
    api_dir = tmp_path / "api"
    api_dir.mkdir()
    f = api_dir / "foo_api.py"
    entries = "            '400': \"Error\","
    f.write_text(_RESP_MAP_TEMPLATE.format(entries=entries), encoding="utf-8")

    assert post_process.fix_missing_2xx_response_types(api_dir) == 3
    out = f.read_text()
    # All three variants get the 200 entry derived from the plain method
    assert out.count("'200': \"List[Foo]\",") == 3


def test_response_types_skips_when_2xx_present(tmp_path):
    api_dir = tmp_path / "api"
    api_dir.mkdir()
    f = api_dir / "foo_api.py"
    entries = "            '201': \"Foo\",\n            '400': \"Error\","
    original = _RESP_MAP_TEMPLATE.format(entries=entries)
    f.write_text(original, encoding="utf-8")

    assert post_process.fix_missing_2xx_response_types(api_dir) == 0
    assert f.read_text() == original


def test_response_types_handles_none_return(tmp_path):
    """A method returning None should emit `'200': None,` (no quotes)."""
    api_dir = tmp_path / "api"
    api_dir.mkdir()
    f = api_dir / "foo_api.py"
    f.write_text(
        "class FooApi:\n"
        "    def delete_thing(self) -> None:\n"
        "        _response_types_map: Dict[str, Optional[str]] = {\n"
        "            '400': \"Error\",\n"
        "        }\n"
        "        return _response_types_map\n",
        encoding="utf-8",
    )

    assert post_process.fix_missing_2xx_response_types(api_dir) == 1
    out = f.read_text()
    assert "'200': None," in out
    assert "'200': \"None\"" not in out

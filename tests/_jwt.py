"""
JWT factories shared by the auth and client tests.

Underscore-prefixed so pytest does not collect it as a test module. Stdlib only —
it must not import common/ or any tb_*_client package, so either side can use it.
"""

import base64
import json
import time


def _make_jwt(claims: dict) -> str:
    """Create a minimal 3-part JWT (header.payload.signature) for testing.

    The header and signature are stubs — only the payload is meaningful.
    """
    header = (
        base64.urlsafe_b64encode(json.dumps({"alg": "HS256", "typ": "JWT"}).encode())
        .rstrip(b"=")
        .decode()
    )
    payload = base64.urlsafe_b64encode(json.dumps(claims).encode()).rstrip(b"=").decode()
    signature = "fakesig"
    return f"{header}.{payload}.{signature}"


def _make_token(exp_offset_s: int, iat_offset_s: int = 0) -> str:
    """Create a JWT with exp = now + exp_offset_s and iat = now + iat_offset_s."""
    now = int(time.time())
    return _make_jwt(
        {
            "exp": now + exp_offset_s,
            "iat": now + iat_offset_s,
            "sub": "user@example.com",
        }
    )


def _make_refresh_token(exp_offset_s: int) -> str:
    """Create a JWT with exp = now + exp_offset_s (for refresh tokens)."""
    now = int(time.time())
    return _make_jwt(
        {
            "exp": now + exp_offset_s,
            "sub": "user@example.com",
        }
    )

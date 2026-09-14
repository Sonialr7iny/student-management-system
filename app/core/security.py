from __future__ import annotations

import hashlib
import secrets

_SALT_BYTES = 16


def hash_password(password: str, salt: bytes | None = None) -> str:
    """Create a PBKDF2-HMAC-SHA256 password representation."""
    if not password:
        raise ValueError("Password cannot be empty")
    salt = salt or secrets.token_bytes(_SALT_BYTES)
    digest = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 120_000)
    return f"{salt.hex()}${digest.hex()}"


def verify_password(password: str, stored_hash: str) -> bool:
    """Verify a password against a stored representation."""
    try:
        salt_hex, digest_hex = stored_hash.split("$", 1)
        salt = bytes.fromhex(salt_hex)
    except ValueError:
        return False
    candidate = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 120_000)
    return secrets.compare_digest(candidate.hex(), digest_hex)

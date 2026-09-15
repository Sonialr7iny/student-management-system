from __future__ import annotations

import time
from functools import wraps
from typing import Any, Callable, ParamSpec, TypeVar

from app.core.exceptions import AuthorizationError
from app.models.entities import Role, User
# from app.models import Role, User

P = ParamSpec("P")
R = TypeVar("R")


def log_call(func: Callable[P, R]) -> Callable[P, R]:
    """Log a function call."""
    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        print(f"[LOG] calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[LOG] finished {func.__name__}")
        return result
    return wrapper


def timed(func: Callable[P, R]) -> Callable[P, R]:
    """Measure execution time."""
    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        start = time.perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            print(f"[TIMER] {func.__name__}: {time.perf_counter() - start:.6f}s")
    return wrapper


def requires_role(*allowed_roles: Role):
    """Decorator factory that checks the current user's role."""
    allowed = set(allowed_roles)

    def decorator(func: Callable[..., R]) -> Callable[..., R]:
        @wraps(func)
        def wrapper(self: Any, *args: Any, **kwargs: Any) -> R:
            user: User | None = getattr(self, "current_user", None)
            if user is None or user.role not in allowed:
                names = ", ".join(role.value for role in allowed)
                raise AuthorizationError(f"{func.__name__} requires: {names}")
            return func(self, *args, **kwargs)
        return wrapper
    return decorator

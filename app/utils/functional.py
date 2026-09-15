from __future__ import annotations

from collections.abc import Callable, Iterable
from typing import TypeVar

T = TypeVar("T")
R = TypeVar("R")


def aggregate(*values: float, operation: str = "sum") -> float:
    """Aggregate variable-length values using a keyword-only operation."""
    if not values:
        return 0.0
    if operation == "sum":
        return sum(values)
    if operation == "max":
        return max(values)
    if operation == "min":
        return min(values)
    if operation == "average":
        return sum(values) / len(values)
    raise ValueError(f"Unsupported operation: {operation}")


def apply_transform(items: Iterable[T], transform: Callable[[T], R]) -> list[R]:
    """Apply a callable to every item (higher-order function)."""
    return list(map(transform, items))


def select(items: Iterable[T], predicate: Callable[[T], bool]) -> list[T]:
    """Keep items matching a predicate."""
    return list(filter(predicate, items))


def make_multiplier(factor: float) -> Callable[[float], float]:
    """Return a closure remembering a factor."""
    def multiply(value: float) -> float:
        return value * factor
    return multiply


def build_message(prefix: str, /, *, suffix: str = "") -> Callable[..., str]:
    """Demonstrate positional-only, keyword-only and **kwargs."""
    def formatter(message: str, **metadata: object) -> str:
        details = ", ".join(f"{k}={v}" for k, v in metadata.items())
        body = f"{prefix}: {message}"
        return body + (f" ({details})" if details else "") + suffix
    return formatter

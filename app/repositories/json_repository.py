from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Generic, TypeVar

from app.core.exceptions import StorageError

T = TypeVar("T")


class JsonRepository(Generic[T]):
    """Generic file-backed JSON repository."""

    def __init__(self, file_path: Path, collection: str):
        self.file_path = file_path
        self.collection = collection
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        self._ensure_file()

    def _ensure_file(self) -> None:
        if not self.file_path.exists():
            self._write_all(
                {"users": [], "students": [], "courses": [], "enrollments": []}
            )

    def _read_all(self) -> dict[str, Any]:
        try:
            with self.file_path.open("r", encoding="utf-8") as f:
                data = json.load(f)
            if not isinstance(data, dict):
                raise ValueError("JSON root must be an object")
            return data
        except (OSError, json.JSONDecodeError, ValueError) as exc:
            raise StorageError(f"Could not read storage: {exc}") from exc

    def _write_all(self, data: dict[str, Any]) -> None:
        temp = self.file_path.with_suffix(".tmp")
        try:
            with temp.open("w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            temp.replace(self.file_path)
        except OSError as exc:
            raise StorageError(f"Could not write storage: {exc}") from exc

    def list(self) -> list[T]:
        return list(self._read_all().get(self.collection, []))

    def replace_all(self, items: list[dict]) -> None:
        data = self._read_all()
        data[self.collection] = items
        self._write_all(data)

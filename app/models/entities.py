from __future__ import annotations

from dataclasses import asdict, dataclass, field
from enum import StrEnum
from uuid import uuid4
from datetime import datetime,timezone


class Role(StrEnum):
    ADMIN = "admin"
    MANAGER="manager"
    USER="user"

class TaskStatus(StrEnum):
    TODO="todo"
    IN_PROGRESS="in progress"
    DONE="done"

@dataclass(slots=True)
class User:
    username: str
    password_hash: str
    role: Role = Role.USER
    id: str = field(default_factory=lambda: str(uuid4()))

    def to_dict(self) -> dict:
        return asdict(self) | {"role": self.role.value}

    @classmethod
    def from_dict(cls, data: dict) -> "User":
        return cls(
            username=data["username"],
            password_hash=data["password_hash"],
            role=Role(data.get("role", Role.ADMIN.value)),
            id=data["id"],
        )


@dataclass(slots=True)
class Task:
    title: str
    project_id: str
    assignee_id: str
    description: str =""
    TaskStatus: TaskStatus = TaskStatus.TODO
    priority: int = 3
    id: str = field(default_factory=lambda: str(uuid4()))
    creeted_at:str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        return cls(**data)


@dataclass(slots=True)
class Project:
    name: str
    description: str
    owner_id: int = 3
    id: str = field(default_factory=lambda: str(uuid4()))

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "Project":
        return cls(**data)




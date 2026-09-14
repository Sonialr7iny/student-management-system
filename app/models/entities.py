from __future__ import annotations

from dataclasses import asdict, dataclass, field
from enum import StrEnum
from uuid import uuid4


class Role(StrEnum):
    ADMIN = "admin"
    TEACHER = "teacher"


@dataclass(slots=True)
class User:
    username: str
    password_hash: str
    role: Role = Role.TEACHER
    id: str = field(default_factory=lambda: str(uuid4()))

    def to_dict(self) -> dict:
        return asdict(self) | {"role": self.role.value}

    @classmethod
    def from_dict(cls, data: dict) -> "User":
        return cls(
            username=data["username"],
            password_hash=data["password_hash"],
            role=Role(data.get("role", Role.TEACHER.value)),
            id=data["id"],
        )


@dataclass(slots=True)
class Student:
    name: str
    student_no: str
    major: str
    id: str = field(default_factory=lambda: str(uuid4()))

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "Student":
        return cls(**data)


@dataclass(slots=True)
class Course:
    code: str
    name: str
    credit_hours: int = 3
    id: str = field(default_factory=lambda: str(uuid4()))

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "Course":
        return cls(**data)


@dataclass(slots=True)
class Enrollment:
    student_id: str
    course_id: str
    grade: float | None = None
    id: str = field(default_factory=lambda: str(uuid4()))

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "Enrollment":
        grade = data.get("grade")
        return cls(
            student_id=data["student_id"],
            course_id=data["course_id"],
            grade=float(grade) if grade is not None else None,
            id=data["id"],
        )

from __future__ import annotations

from app.core.config import settings
from app.models import Enrollment
from app.repositories.json_repository import JsonRepository


class EnrollmentRepository:
    def __init__(self):
        self._repo = JsonRepository[Enrollment](settings.data_file, "enrollments")

    def list(self) -> list[Enrollment]:
        return [Enrollment.from_dict(item) for item in self._repo.list()]

    def find(self, student_id: str, course_id: str) -> Enrollment | None:
        return next(
            (
                e for e in self.list()
                if e.student_id == student_id and e.course_id == course_id
            ),
            None,
        )

    def by_student(self, student_id: str) -> list[Enrollment]:
        return [e for e in self.list() if e.student_id == student_id]

    def save(self, enrollment: Enrollment) -> Enrollment:
        items = [e for e in self.list() if e.id != enrollment.id]
        items.append(enrollment)
        self._repo.replace_all([e.to_dict() for e in items])
        return enrollment

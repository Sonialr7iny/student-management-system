from __future__ import annotations

from app.core.exceptions import DuplicateError, ValidationError
from app.models import Role, Student, User
from app.repositories import StudentRepository
from app.utils import requires_role, timed


class StudentService:
    def __init__(self, student_repository: StudentRepository, current_user: User | None = None):
        self.repository = student_repository
        self.current_user = current_user

    @requires_role(Role.ADMIN, Role.TEACHER)
    def add_student(self, name: str, student_no: str, major: str = "") -> Student:
        """Create a student after checking the unique student number."""
        if not name.strip() or not student_no.strip():
            raise ValidationError("Name and student number are required")
        if self.repository.get_by_number(student_no.strip()):
            raise DuplicateError("Student number already exists")
        return self.repository.save(Student(name.strip(), student_no.strip(), major.strip()))

    def list_students(self, *, major: str | None = None) -> list[Student]:
        """List students; major is a keyword-only filter."""
        students = self.repository.list()
        if major:
            students = [s for s in students if s.major.lower() == major.lower()]
        return sorted(students, key=lambda s: s.name.lower())

    @timed
    def get_student(self, student_id: str) -> Student:
        return self.repository.get(student_id)

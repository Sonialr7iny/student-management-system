from app.core.config import settings
from app.core.exceptions import NotFoundError
from app.models import Student
from app.repositories.json_repository import JsonRepository


class StudentRepository:
    def __init__(self):
        self._repo = JsonRepository[Student](settings.data_file, "students")

    def list(self) -> list[Student]:
        return [Student.from_dict(item) for item in self._repo.list()]

    def get(self, student_id: str) -> Student:
        for student in self.list():
            if student.id == student_id:
                return student
        raise NotFoundError(f"Student not found: {student_id}")

    def get_by_number(self, student_no: str) -> Student | None:
        return next((s for s in self.list() if s.student_no == student_no), None)

    def save(self, student: Student) -> Student:
        items = [s for s in self.list() if s.id != student.id]
        items.append(student)
        self._repo.replace_all([s.to_dict() for s in items])
        return student

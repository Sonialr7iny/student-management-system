from app.core.config import settings
from app.core.exceptions import NotFoundError
from app.models import Course
from app.repositories.json_repository import JsonRepository


class CourseRepository:
    def __init__(self):
        self._repo = JsonRepository[Course](settings.data_file, "courses")

    def list(self) -> list[Course]:
        return [Course.from_dict(item) for item in self._repo.list()]

    def get(self, course_id: str) -> Course:
        for course in self.list():
            if course.id == course_id:
                return course
        raise NotFoundError(f"Course not found: {course_id}")

    def get_by_code(self, code: str) -> Course | None:
        return next((c for c in self.list() if c.code == code), None)

    def save(self, course: Course) -> Course:
        items = [c for c in self.list() if c.id != course.id]
        items.append(course)
        self._repo.replace_all([c.to_dict() for c in items])
        return course

from __future__ import annotations

from app.core.exceptions import DuplicateError, ValidationError
from app.models import Course, Enrollment, Role, User
from app.repositories import CourseRepository, EnrollmentRepository, StudentRepository
from app.utils import requires_role


class CourseService:
    def __init__(
        self,
        course_repository: CourseRepository,
        enrollment_repository: EnrollmentRepository,
        student_repository: StudentRepository,
        current_user: User | None = None,
    ):
        self.course_repository = course_repository
        self.enrollment_repository = enrollment_repository
        self.student_repository = student_repository
        self.current_user = current_user

    @requires_role(Role.ADMIN, Role.TEACHER)
    def add_course(self, code: str, name: str, credit_hours: int = 3) -> Course:
        """Create a course after validating its code and credit hours."""
        code = code.strip().upper()
        if not code or not name.strip():
            raise ValidationError("Course code and name are required")
        if credit_hours < 1:
            raise ValidationError("Credit hours must be positive")
        if self.course_repository.get_by_code(code):
            raise DuplicateError("Course code already exists")
        return self.course_repository.save(Course(code, name.strip(), credit_hours))

    def list_courses(self) -> list[Course]:
        return sorted(self.course_repository.list(), key=lambda c: c.code)

    @requires_role(Role.ADMIN, Role.TEACHER)
    def enroll(self, student_no: str, course_code: str) -> Enrollment:
        student = self.student_repository.get_by_number(student_no.strip())
        course = self.course_repository.get_by_code(course_code.strip().upper())
        if student is None:
            raise ValidationError("Student number does not exist")
        if course is None:
            raise ValidationError("Course code does not exist")
        if self.enrollment_repository.find(student.id, course.id):
            raise DuplicateError("Student is already enrolled")
        return self.enrollment_repository.save(Enrollment(student.id, course.id))

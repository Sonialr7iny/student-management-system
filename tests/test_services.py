import tempfile
import unittest
from pathlib import Path

from app.core.config import settings
from app.core.exceptions import DuplicateError, ValidationError
from app.models import Role
from app.repositories import (
    CourseRepository,
    EnrollmentRepository,
    StudentRepository,
    UserRepository,
)
from app.services import AuthService, CourseService, ReportService, StudentService


class TestServices(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.old = settings.data_file
        object.__setattr__(settings, "data_file", Path(self.tmp.name) / "store.json")

        self.user_repo = UserRepository()
        self.student_repo = StudentRepository()
        self.course_repo = CourseRepository()
        self.enrollment_repo = EnrollmentRepository()

        auth = AuthService(self.user_repo)
        self.user = auth.register("teacher", "password123", role=Role.TEACHER)

        self.students = StudentService(self.student_repo, self.user)
        self.courses = CourseService(
            self.course_repo, self.enrollment_repo, self.student_repo, self.user
        )

    def tearDown(self):
        object.__setattr__(settings, "data_file", self.old)
        self.tmp.cleanup()

    def test_student_course_grade_report(self):
        student = self.students.add_student("Ali", "S100", "CS")
        course = self.courses.add_course("CS101", "Python", 3)

        enrollment = self.courses.enroll(student.student_no, course.code)
        enrollment.grade = 90
        self.enrollment_repo.save(enrollment)

        report = ReportService(
            self.student_repo, self.course_repo, self.enrollment_repo
        )
        self.assertEqual(report.student_average("S100"), 90)
        self.assertEqual(report.top_students(1)[0][0].student_no, "S100")

    def test_duplicate_student_rejected(self):
        self.students.add_student("Sara", "S200", "SE")
        with self.assertRaises(DuplicateError):
            self.students.add_student("Sara 2", "S200", "SE")

    def test_invalid_course_rejected(self):
        with self.assertRaises(ValidationError):
            self.courses.add_course("", "Python")


if __name__ == "__main__":
    unittest.main()

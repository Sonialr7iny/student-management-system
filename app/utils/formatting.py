# from collections.abc import Iterable

# from app.models import Course, Student


# def format_students(students: Iterable[Student]) -> str:
#     lines = [
#         f"{s.student_no:<10} | {s.name:<25} | {s.major}"
#         for s in students
#     ]
#     return "\n".join(lines) if lines else "No students."


# def format_courses(courses: Iterable[Course]) -> str:
#     lines = [
#         f"{c.code:<8} | {c.name:<25} | {c.credit_hours} credits"
#         for c in courses
#     ]
#     return "\n".join(lines) if lines else "No courses."

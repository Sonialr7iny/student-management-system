import unittest

from app.core.security import hash_password, verify_password
from app.models import Role


class TestCore(unittest.TestCase):
    def test_password_hash(self):
        stored = hash_password("StrongPass123!")
        self.assertTrue(verify_password("StrongPass123!", stored))
        self.assertFalse(verify_password("wrong", stored))

    def test_enum(self):
        self.assertEqual(Role.TEACHER.value, "teacher")


if __name__ == "__main__":
    unittest.main()

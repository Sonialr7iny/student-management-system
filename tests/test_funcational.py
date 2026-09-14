import unittest

from app.utils.functional import (
    aggregate,
    apply_transform,
    build_message,
    make_multiplier,
    select,
)


class TestFunctional(unittest.TestCase):
    def test_args_and_keyword_only(self):
        self.assertEqual(aggregate(10, 20, 30), 60)
        self.assertEqual(aggregate(10, 20, 30, operation="average"), 20)

    def test_higher_order(self):
        self.assertEqual(apply_transform([1, 2, 3], lambda x: x * 2), [2, 4, 6])
        self.assertEqual(select([1, 2, 3, 4], lambda x: x % 2 == 0), [2, 4])

    def test_closure(self):
        triple = make_multiplier(3)
        self.assertEqual(triple(7), 21)

    def test_kwargs(self):
        message = build_message("INFO", suffix="!")
        self.assertEqual(message("created", user_id=42), "INFO: created (user_id=42)!")


if __name__ == "__main__":
    unittest.main()

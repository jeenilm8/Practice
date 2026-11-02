import unittest

from practice import add, factorial, is_even


class TestPracticeFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(10, 20), 30)

    def test_is_even(self):
        self.assertTrue(is_even(8))
        self.assertFalse(is_even(7))

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)

    def test_factorial_negative_number(self):
        with self.assertRaises(ValueError):
            factorial(-1)


if __name__ == "__main__":
    unittest.main()

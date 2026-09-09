import unittest

from app import add, multiply


class TestAdd(unittest.TestCase):
    def test_adds_positive_integers(self):
        self.assertEqual(add(2, 3), 5)

    def test_adds_negative_integers(self):
        self.assertEqual(add(-2, -3), -5)


class TestMultiply(unittest.TestCase):
    def test_multiplies_positive_integers(self):
        self.assertEqual(multiply(2, 3), 6)

    def test_multiplies_negative_integers(self):
        self.assertEqual(multiply(-2, -3), 6)

    def test_multiplies_mixed_sign_integers(self):
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(2, -3), -6)


if __name__ == "__main__":
    unittest.main()

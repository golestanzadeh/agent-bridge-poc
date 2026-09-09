import unittest

from app import add


class TestAdd(unittest.TestCase):
    def test_adds_positive_integers(self):
        self.assertEqual(add(2, 3), 5)

    def test_adds_negative_integers(self):
        self.assertEqual(add(-2, -3), -5)


if __name__ == "__main__":
    unittest.main()

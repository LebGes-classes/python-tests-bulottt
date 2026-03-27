import unittest
from main import add, subtract, multiply, divide


class TestMain(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 5), 7)
        self.assertEqual(add(2, 0), 2)
        self.assertEqual(add(-3.5, 2.5), -1)
        self.assertEqual(add(-2, -7), -9)

    def test_add_type_error(self):
        with self.assertRaises(TypeError):
            add(2, "5")

    def test_subtract(self):
        self.assertEqual(subtract(10, 2), 8)
        self.assertEqual(subtract(10.1, 5.1), 5)
        self.assertEqual(subtract(-2, 3), -5)

    def test_subtract_type_error(self):
        with self.assertRaises(TypeError):
            subtract(10, "2")

    def test_multiply(self):
        self.assertEqual(multiply(0, 1), 0)
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 4), -8)

    def test_multiply_type_error(self):
        with self.assertRaises(TypeError):
            multiply("1", 2)

    def test_divide(self):
        self.assertEqual(divide(6, 2), 3)
        self.assertEqual(divide(3, 2), 1.5)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(1, 0)

    def test_divide_type_error(self):
        with self.assertRaises(TypeError):
            divide("-10", 2)


if __name__ == "__main__":
    unittest.main()

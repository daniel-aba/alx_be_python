import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Set up a SimpleCalculator instance for each test."""
        self.calc = SimpleCalculator()

    def test_add_method(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(5, 3), 8)
        self.assertEqual(self.calc.add(-5, 3), -2)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(10, -10), 0)
        self.assertEqual(self.calc.add(2.5, 3.5), 6.0)

    def test_subtract_method(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(5, 10), -5)
        self.assertEqual(self.calc.subtract(5, -5), 10)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(7.5, 2.5), 5.0)

    def test_multiply_method(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(4, 5), 20)
        self.assertEqual(self.calc.multiply(-2, 5), -10)
        self.assertEqual(self.calc.multiply(0, 100), 0)
        self.assertEqual(self.calc.multiply(-3, -3), 9)
        self.assertEqual(self.calc.multiply(2.5, 2), 5.0)

    def test_divide_method(self):
        """Test the division method, including the zero case."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(10, 4), 2.5)
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertIsNone(self.calc.divide(10, 0))

if __name__ == "__main__":
    unittest.main()
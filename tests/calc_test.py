import unittest

from app.triangle import TriangleCalculator


class MyCalculatorTest(unittest.TestCase):
    """Тесты для класса TriangleCalculator (простые случаи)."""

    def test_triangle1(self):
        """Равносторонний треугольник 1-1-1."""
        calculator = TriangleCalculator(1, 1, 1)
        result = calculator.get_area()
        self.assertEqual(result, 0.43)

    def test_triangle2(self):
        """Прямоугольный треугольник 3-4-5."""
        calculator = TriangleCalculator(3, 4, 5)
        result = calculator.get_area()
        self.assertEqual(result, 6.0)


if __name__ == '__main__':
    unittest.main()
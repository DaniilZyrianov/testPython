import unittest

from parameterized import parameterized

from app.triangle import TriangleCalculator


class TriangleCalculatorTest(unittest.TestCase):
    """Параметризованные тесты для класса TriangleCalculator."""

    @parameterized.expand([
        # Валидные треугольники: (a, b, c, ожидаемая площадь)
        (3, 4, 5, 6.0),
        (5, 5, 5, 10.83),
        (5, 5, 8, 12.0),
        (1, 1, 1, 0.43),
        (99, 99, 99, 4243.96),
    ])
    def test_valid(self, a, b, c, expected):
        """Проверяет площадь для корректных треугольников."""
        calculator = TriangleCalculator(a, b, c)
        self.assertEqual(calculator.get_area(), expected)


if __name__ == '__main__':
    unittest.main()
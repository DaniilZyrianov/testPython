import unittest
from parameterized import parameterized

from app.triangle import TriangleCalculator, SideException

class TestGetArea(unittest.TestCase):
    """Параметризованные тесты для метода get_area."""

    @parameterized.expand([
        ("3-4-5 (прямоугольный)",  3, 4, 5,  6.0),
        ("5-5-5 (равносторонний)", 5, 5, 5,  10.83),
        ("5-5-6 (равнобедренный)", 5, 5, 6,  12.0),
        ("7-8-9 (разносторонний)", 7, 8, 9,  26.83),
        ("1-1-1 (минимум)",        1, 1, 1,  0.43),
    ])
    def test_get_area(self, name, a, b, c, expected):
        """Проверяет площадь для разных треугольников."""
        calculator = TriangleCalculator(a, b, c)
        self.assertEqual(calculator.get_area(), expected)

class TestGetPerimeter(unittest.TestCase):
    """Параметризованные тесты для метода get_perimeter."""

    @parameterized.expand([
        ("3-4-5",             3, 4, 5, 12.0),
        ("5-5-5",             5, 5, 5, 15.0),
        ("5-5-6",             5, 5, 6, 16.0),
        ("7-8-9",             7, 8, 9, 24.0),
        ("99.99-99.99-99.99", 99.99, 99.99, 99.99, 299.97),
    ])
    def test_get_perimeter(self, name, a, b, c, expected):
        """Проверяет периметр для разных треугольников."""
        calculator = TriangleCalculator(a, b, c)
        self.assertEqual(calculator.get_perimeter(), expected)

class TestGetTriangleType(unittest.TestCase):
    """Параметризованные тесты для метода get_triangle_type."""

    @parameterized.expand([
        ("3-4-5 (scalene)",     3, 4, 5, "scalene"),
        ("5-5-5 (equilateral)", 5, 5, 5, "equilateral"),
        ("5-5-6 (isosceles)",   5, 5, 6, "isosceles"),
        ("6-6-6 (equilateral)", 6, 6, 6, "equilateral"),
        ("7-8-9 (scalene)",     7, 8, 9, "scalene"),
    ])
    def test_get_triangle_type(self, name, a, b, c, expected):
        """Проверяет тип треугольника для разных случаев."""
        calculator = TriangleCalculator(a, b, c)
        self.assertEqual(calculator.get_triangle_type(), expected)
# ==================== НЕГАТИВНЫЕ ТЕСТЫ ПЕРИМЕТРА ====================

class TestGetPerimeterNegative(unittest.TestCase):
    """Негативные тесты для get_perimeter."""

    @parameterized.expand([
        ("сторона меньше 1", 0.5, 5, 5),
        ("сторона равна 0",  0,   5, 5),
        ("отрицательная",   -1,   2, 3),
        ("сторона = 100",    100, 50, 50),
        ("вырожденный",      3,   4, 7),
    ])
    def test_get_perimeter_invalid(self, name, a, b, c):
        """Проверяет, что выбрасывается SideException."""
        calculator = TriangleCalculator(a, b, c)
        with self.assertRaises(SideException):
            calculator.get_perimeter()


# ==================== НЕГАТИВНЫЕ ТЕСТЫ ТИПА ====================

class TestGetTriangleTypeNegative(unittest.TestCase):
    """Негативные тесты для get_triangle_type."""

    @parameterized.expand([
        ("сторона меньше 1", 0.5, 5, 5),
        ("сторона равна 0",  0,   5, 5),
        ("отрицательная",   -1,   2, 3),
        ("сторона = 100",    100, 50, 50),
        ("вырожденный",      3,   4, 7),
    ])
    def test_get_triangle_type_invalid(self, name, a, b, c):
        """Проверяет, что выбрасывается SideException."""
        calculator = TriangleCalculator(a, b, c)
        with self.assertRaises(SideException):
            calculator.get_triangle_type()


class TestTriangleTypes(unittest.TestCase):
    """Тесты на все три типа треугольников."""

    def test_equilateral(self):
        calculator = TriangleCalculator(5, 5, 5)
        self.assertEqual(calculator.get_triangle_type(), "equilateral")

    def test_isosceles(self):
        calculator = TriangleCalculator(5, 5, 6)
        self.assertEqual(calculator.get_triangle_type(), "isosceles")

    def test_scalene(self):
        calculator = TriangleCalculator(3, 4, 5)
        self.assertEqual(calculator.get_triangle_type(), "scalene")

if __name__ == '__main__':
    unittest.main()

import unittest

from app.triangle import TriangleCalculator, SideException


class TestPositiveCases(unittest.TestCase):
    """Позитивные тесты: проверяем корректный расчёт площади."""

    def test_classic_right_triangle_3_4_5(self):
        """
        П.1 из чек-листа.
        Классический прямоугольный треугольник 3-4-5.
        Ожидаемая площадь: 6.0.
        """
        calculator = TriangleCalculator(3, 4, 5)
        self.assertEqual(calculator.get_area(), 6.0)

    def test_equilateral_triangle_5_5_5(self):
        """
        П.2 из чек-листа.
        Равносторонний треугольник со стороной 5.
        Ожидаемая площадь: 10.83.
        """
        calculator = TriangleCalculator(5, 5, 5)
        self.assertEqual(calculator.get_area(), 10.83)

    def test_isosceles_triangle_5_5_6(self):
        """
        П.3 из чек-листа.
        Равнобедренный треугольник 5-5-6.
        Ожидаемая площадь: 12.0.
        """
        calculator = TriangleCalculator(5, 5, 6)
        self.assertEqual(calculator.get_area(), 12.0)


class TestNegativeCases(unittest.TestCase):
    """Негативные тесты: проверяем, что выбрасывается SideException."""

    def test_side_less_than_one(self):
        """
        Н.1 из чек-листа.
        Сторона меньше 1 (0.5) — недопустимое значение.
        Ожидается SideException.
        """
        calculator = TriangleCalculator(0.5, 5, 5)
        with self.assertRaises(SideException):
            calculator.get_area()

    def test_side_equal_zero(self):
        """
        Н.2 из чек-листа.
        Сторона равна 0 — недопустимое значение.
        Ожидается SideException.
        """
        calculator = TriangleCalculator(0, 5, 5)
        with self.assertRaises(SideException):
            calculator.get_area()

    def test_degenerate_triangle_3_4_7(self):
        """
        Н.7 из чек-листа.
        Вырожденный треугольник: сумма двух сторон равна третьей (3+4=7).
        Треугольник не существует. Ожидается SideException.
        """
        calculator = TriangleCalculator(3, 4, 7)
        with self.assertRaises(SideException):
            calculator.get_area()


if __name__ == '__main__':
    unittest.main()
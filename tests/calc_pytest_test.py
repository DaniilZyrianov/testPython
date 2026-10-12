from app.triangle import TriangleCalculator
import pytest
class TestClass:
    # Creating param test case
@pytest.mark.parametrize('a,b,c,expected',
                         [(3, 4, 5, 6.0),
                          (5, 5, 5, 10.83),
                          (5, 5, 8, 12.0),
                          (1, 1, 1, 0.43),
                          (99, 99, 99, 4243.96)])
def test_param(a, b, c, expected):
    calculator = TriangleCalculator(a, b, c)
    actual = calculator.get_area()
    assert expected == actual
    @pytest.mark.skip(reason= 'пропуск')
    def test_triangle1():
     calculator = TriangleCalculator(1, 1, 1)
     result = calculator.get_area()
     assert result == 0.43
def test_triangle2():
    calculator = TriangleCalculator(3, 4, 5)
    result = calculator.get_area()
    assert result == 6.00    


    if __name__ == "__main__":
        pytest.main()


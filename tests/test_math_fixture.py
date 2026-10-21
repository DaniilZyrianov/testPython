import pytest
def add_numbers(*args):
    """Складывает любое количество чисел."""
    return sum(args)

@pytest.fixture(params=[
    ([2, 3], 5),              # Два числа
    ([-5, 5], 0),             # Разные знаки
    ([1, 2, 3, 4], 10),       # Три и более чисел
    ([0, 0, 0], 0),           # Все нули
    ([10, -5, 0, 5], 10)      # Смешанные с нулём
])
def numbers_data(request):
    """
    Параметризованная фикстура.
    Возвращает кортеж: (набор чисел, ожидаемая сумма).
    Механизм params автоматически запускает тест для каждого набора.
    """
    return request.param

def test_add_numbers_with_fixture(numbers_data):
    """
    Тест использует параметризованную фикстуру.
    Запустится 5 раз (по количеству params в фикстуре).
    """
    numbers, expected = numbers_data
    assert add_numbers(*numbers) == expected

def test_add_two_numbers():
    """Сложение двух положительных чисел."""
    assert add_numbers(2, 3) == 5

def test_add_multiple_numbers():
    """Сложение трех и более чисел с разными знаками."""
    assert add_numbers(10, -5, 0, 5) == 10

def test_add_with_zero():
    """Сложение чисел, включая нули."""
    assert add_numbers(0, 0, 0) == 0
    assert add_numbers(5, 0, 5) == 10
if __name__ == "__main__":
    pytest.main([__file__, "-v"])

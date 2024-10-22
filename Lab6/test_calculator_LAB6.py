import unittest
from classes.class_calc_LAB2 import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    # Завдання 1: Тестування Додавання
    def test_addition_positive_numbers(self):
        result = self.calculator.perform_calculation(3, '+', 5)
        self.assertEqual(result, 8)

    def test_addition_negative_numbers(self):
        result = self.calculator.perform_calculation(-3, '+', -5)
        self.assertEqual(result, -8)

    # Завдання 2: Тестування Віднімання
    def test_subtraction_positive_numbers(self):
        result = self.calculator.perform_calculation(10, '-', 5)
        self.assertEqual(result, 5)

    def test_subtraction_negative_result(self):
        result = self.calculator.perform_calculation(5, '-', 10)
        self.assertEqual(result, -5)

    # Завдання 3: Тестування Множення
    def test_multiplication_positive_numbers(self):
        result = self.calculator.perform_calculation(4, '*', 5)
        self.assertEqual(result, 20)

    def test_multiplication_with_zero(self):
        result = self.calculator.perform_calculation(0, '*', 10)
        self.assertEqual(result, 0)

    def test_multiplication_negative_numbers(self):
        result = self.calculator.perform_calculation(-4, '*', 5)
        self.assertEqual(result, -20)

    # Завдання 4: Тестування Ділення
    def test_division_positive_numbers(self):
        result = self.calculator.perform_calculation(10, '/', 2)
        self.assertEqual(result, 5)

    def test_division_negative_numbers(self):
        result = self.calculator.perform_calculation(-9, '/', 3)
        self.assertEqual(result, -3)

    def test_division_by_zero(self):
        result = self.calculator.perform_calculation(10, '/', 0)
        self.assertIsNone(result)  # Перевіряємо, що повертається None у випадку ділення на нуль

    # Завдання 5: Тестування Обробки Помилок
    def test_invalid_operator(self):
        result = self.calculator.perform_calculation(10, '#', 2)
        self.assertIsNone(result)  # Перевірка на некоректний оператор


if __name__ == '__main__':
    unittest.main()
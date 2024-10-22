from const_GlobalVariables.operators_LAB1 import OPERATORS
import math

# Основна функція обчислень
def calculate(num1, operator, num2=None):
    match operator:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case '/':
            match num2:
                case 0:
                    raise ZeroDivisionError("Помилка: ділення на нуль!")
                case _:
                    return num1 / num2
        case '^':
            return num1 ** num2
        case '%':
            return num1 % num2
        case '√':
            match num1:
                case n if n < 0:
                    raise ValueError("Помилка: не можна знайти квадратний корінь з від'ємного числа!")
                case _:
                    return math.sqrt(num1)
        case _:
            raise ValueError("Неправильний оператор")

# Перевірка правильності оператора
def is_valid_operator(operator):
    return operator in OPERATORS

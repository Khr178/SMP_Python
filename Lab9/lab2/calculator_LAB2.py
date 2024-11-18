from DAL.memory_LAB2 import log_operation, log_history

class Calculator:
   def calculate(self, num1, operator, num2=None):
    match operator:
        case '+':
            result = num1 + num2
        case '-':
            result = num1 - num2
        case '*':
            result = num1 * num2
        case '/':
            if num2 == 0:
                raise ZeroDivisionError("Ділення на нуль!")
            result = num1 / num2
        case '^':
            result = num1 ** num2
        case '%':
            result = num1 % num2
        case '√':
            result = num1 ** 0.5
        case _:
            raise ValueError("Невірний оператор")
    
    # Формування виразу
    expression = f"{num1} {operator} {num2 if operator != '√' else ''}"

    # Логування операції
    log_operation(f"{expression} = {result}")
    log_history(expression, result)

    return result


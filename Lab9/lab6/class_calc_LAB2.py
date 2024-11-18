from Shared.AppSettings_LAB1 import decimal_places
from Shared.logs.logger_LAB1 import log_operation, log_history, show_history
from functions_LAB1 import calculate

class Calculator:
    def __init__(self):
        self.memory = None
        self.decimal_places = decimal_places

    def get_input(self):
        try:
            num1 = float(input("Введіть перше число: "))
            operator = input("Введіть оператор (+, -, *, /, ^, %, √): ")
            num2 = None
            if operator != '√':
                num2 = float(input("Введіть друге число: "))
            return num1, operator, num2
        except ValueError:
            print("Неправильний ввід. Спробуйте знову.")
            return self.get_input()

    def is_valid_operator(self, operator):
        return operator in ['+', '-', '*', '/', '^', '%', '√']

    def perform_calculation(self, num1, operator, num2):
        try:
            result = calculate(num1, operator, num2)
            return round(result, self.decimal_places)
        except ZeroDivisionError:
            print("Помилка: Ділення на нуль неможливе.")
        except ValueError as e:
            print(f"Помилка: {e}")
        except Exception as e:
            print(f"Виникла непередбачена помилка: {e}")
        return None

    def ask_to_continue(self):
        return input("Бажаєте виконати ще одне обчислення? (так/ні): ").lower() == 'так'

    def store_in_memory(self, result):
        self.memory = result
        print(f"Результат {result} збережений у пам'яті.")

    def recall_memory(self):
        if self.memory is not None:
            print(f"Збережене значення: {self.memory}")
            return self.memory
        else:
            print("Пам'ять порожня.")
            return None

    def run(self):
        print(f"Результати відображатимуться з {self.decimal_places} десятковими знаками.")
        while True:
            num1, operator, num2 = self.get_input()

            if not self.is_valid_operator(operator):
                print("Недійсний оператор. Спробуйте ще раз. Ви можете використовувати тільки +, -, *, /, ^, %, √")
                continue

            result = self.perform_calculation(num1, operator, num2)
            if result is not None:
                print(f"Результат: {result}")
                self.store_in_memory(result)

                expression = f"{num1} {operator} {num2 if operator != '√' else ''}"
                log_operation(f"{expression} = {result}")
                log_history(expression, result)

            if input("Бажаєте переглянути історію розрахунків? (так/ні): ").lower() == 'так':
                show_history()

            if not self.ask_to_continue():
                break
            
                

                

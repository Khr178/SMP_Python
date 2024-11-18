from functions_LAB1 import calculate, is_valid_operator
from Shared.AppSettings_LAB1 import decimal_places
from Shared.logs.logger_LAB1 import log_operation, log_history, show_history

def get_input():
    try:
        num1 = float(input("Введіть перше число: "))
        operator = input("Введіть оператор (+, -, *, /, ^, %, √): ")
        num2 = None
        if operator != '√':
            num2 = float(input("Введіть друге число: "))
        return num1, operator, num2
    except ValueError:
        print("Неправильний ввід. Спробуйте знову.")
        return get_input()

def store_in_memory(result):
    global memory
    memory = result
    print(f"Результат {result} збережений у пам'яті.")

def recall_memory():
    if memory is not None:
        print(f"Збережене значення: {memory}")
        return memory
    else:
        print("Пам'ять порожня.")
        return None

def ask_to_continue():
    return input("Бажаєте виконати ще одне обчислення? (так/ні): ").lower() == 'так'

def is_valid_operator(operator):
    return operator in ['+', '-', '*', '/', '^', '%', '√']

def run():
    print(f"Результати відображатимуться з  {decimal_places} з десятковими знаками.")
    while True:
        num1, operator, num2 = get_input()

        match is_valid_operator(operator):
            case False:
                print("Недійсний оператор. Спробуйте ще раз. Ви можете використовувати тільки +, -, *, /, ^, %, √ ")
                continue
            case True:
                try:
                    result = calculate(num1, operator, num2)
                    result = round(result, decimal_places)
                    print(f"Результат: {result}")
                    store_in_memory(result)

                    expression = f"{num1} {operator} {num2 if operator != '√' else ''}"
                    log_operation(f"{expression} = {result}")
                    log_history(expression, result)

                except (ZeroDivisionError, ValueError) as e:
                    print(e)

        match input("Бажаєте переглянути історію розрахунків? (так/ні): ").lower():
            case 'так':
                show_history()
            case _:
                pass

        match ask_to_continue():
            case False:
                break

if __name__ == "__main__":
    run()

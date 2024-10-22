from functions_LAB1 import calculate, is_valid_operator
from Shared.AppSettings_LAB1 import decimal_places
from Shared.logs.logger_LAB1 import log_operation, log_history, show_history
from classes.class_calc_LAB2 import Calculator
from BLL.calculator_LAB2 import Calculator
from BLL.validator_LAB2 import is_valid_operator
from DAL.memory_LAB2 import store_in_memory, recall_memory, show_history
from Shared.AppSettings_LAB1 import decimal_places
from UI.console_interface_LAB3 import start_console_interface
from UI.cli_LAB4 import CLI
from BLL.ascii_art_generator_LAB4 import ArtGenerator
from DAL.file_operations_LAB4 import FileManager
from Shared.utils2_LAB4 import align_text
from colorama import init


# Пам'ять для збереження результатів
memory = None


def main():
    cli = CLI()

    while True:
        text = cli.get_user_input()
        width, height = cli.get_art_dimensions()
        alignment = cli.get_alignment()
        custom_symbol = cli.get_custom_symbol()
        color_option = cli.get_color_option()

        art_generator = ArtGenerator()
        ascii_art = art_generator.generate_art(text, width, height, custom_symbol, color_option)

        aligned_art = align_text(ascii_art, alignment, width)

        print("\nПопередній перегляд ASCII-арту:")
        cli.display_art(aligned_art)

        if cli.get_save_choice():
            filename = cli.get_filename()
            if FileManager.save_to_file(aligned_art, filename):
                print(f"ASCII-арт збережено у файл {filename}")
            else:
                print("Помилка при збереженні файлу.")

        if input("Створити ще один ASCII-арт? (y/n): ").lower() != 'y':
            break

    print("Дякуємо за використання ASCII Art генератора!")



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

def calculator():
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
    start_console_interface()



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
from UI.user_interface_LAB7 import UserInterface
import matplotlib.pyplot as plt
from DAL.data_loader_LAB8 import load_and_preprocess
from BLL.data_explorer_LAB8 import explore_data
from UI.visualizations_LAB8 import plot_combined_chart, plot_histogram




from library.console_menu import ConsoleMenu
from library.facade import LabFacade
from library.logger import Logger


class Runner:
    """
    Основний клас runner, який забезпечує уніфікований інтерфейс для виконання всіх лабораторних робіт.
    Реалізує шаблон facade, щоб спростити інтерфейс для запуску різних лабораторних робіт.
    """

    def __init__(self):
        """Ініціалізація основного класу з меню та патерном"""
        self.logger = Logger()
        self.facade = LabFacade()
        self.menu = ConsoleMenu(
            "Laboratory Works Runner",
            "Please select a lab to run"
        )
        self._setup_menu()

    def _setup_menu(self):
        """Налаштуйте пункти меню з відповідними функціями"""
        self.menu.add_item("Lab 1: Simple Operations", self.facade.execute_lab1)
        self.menu.add_item("Lab 2: Calculator", self.facade.execute_lab2)
        self.menu.add_item("Lab 3: Console Interface", self.facade.execute_lab3)
        self.menu.add_item("Lab 4: ASCII Art", self.facade.execute_lab4)
        self.menu.add_item("Lab 5: 3D Shapes", self.facade.execute_lab5)
        self.menu.add_item("Lab 6: Unit Tests", self.facade.execute_lab6)
        self.menu.add_item("Lab 7: User Repository", self.facade.execute_lab7)
        self.menu.add_item("Lab 8: Data Visualization", self.facade.execute_lab8)

    @Logger().log_function_call
    def run(self):
        """Запустіть runner і покажіть меню"""
        try:
            self.menu.show()
        except KeyboardInterrupt:
            print("\nExiting the program...")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            raise


# Пам'ять для збереження результатів
memory = None

def main8():
    data = load_and_preprocess('Data/games_cleaned.csv')

    explore_data(data)

    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    plot_combined_chart(axes[0], data)
    plot_histogram(axes[1], data, 'avg_mmr', 'Гістограма середнього MMR', 'skyblue')
    plot_histogram(axes[2], data, 'duration', 'Гістограма тривалості ігор', 'salmon')

    fig.suptitle('Результати ігор та статистика')
    plt.tight_layout()
    plt.subplots_adjust(top=0.88)
    plt.savefig('Data/game_results_and_statistics.png')
    plt.show()

def main7():
    ui = UserInterface()
    ui.menu()


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
   runner = Runner()
   runner.run()






from library.menu_interface import MenuInterface
from library.input_validator import InputValidator


class ConsoleMenu(MenuInterface):
    """Реалізація консольного меню"""

    def __init__(self, title, subtitle):
        self.title = title
        self.subtitle = subtitle
        self.items = {}
        self.running = True

    def add_item(self, name, function):
        """Додавання пункту меню з назвою та пов’язаною функцією"""
        next_index = len(self.items) + 1
        self.items[next_index] = (name, function)

    def show(self):
        """Відображення меню та обробка введених даних користувача"""
        while self.running:
            self._display_menu()
            self._handle_choice()

    def _display_menu(self):
        """Відображення пунктів меню"""
        print(f"\n{'=' * 50}")
        print(f"{self.title.center(50)}")
        print(f"{self.subtitle.center(50)}")
        print(f"{'=' * 50}\n")

        for index, (name, _) in self.items.items():
            print(f"{index}. {name}")
        print("\n0. Exit")

    def _handle_choice(self):
        """Керування вибором меню користувача"""
        choice = InputValidator.validate_number_input(
            "\nEnter your choice: ",
            min_value=0,
            max_value=len(self.items)
        )

        if choice == 0:
            self.running = False
            print("\nGoodbye!")
        else:
            try:
                print(f"\nExecuting: {self.items[choice][0]}")
                self.items[choice][1]()
            except Exception as e:
                print(f"Error executing command: {str(e)}")
            input("\nPress Enter to continue...")
from prettytable import PrettyTable
from colorama import Fore, Style
from DAL.user_api_connector_LAB7 import UserAPIConnector
from BLL.user_repository_LAB7 import UserRepository
from Shared.utilities_LAB7 import validate_entry
from DAL.file_saver_LAB7 import FileSaver  # Імпортуємо FileSaver

class UserInterface:
    def __init__(self, user_repository):
        self.user_repository = user_repository
        self.history = []

    def display_users(self):
        users = self.user_repository.get_all_users()
        table = PrettyTable()
        table.field_names = ["ID", "Name", "Username", "Email"]
        for user in users:
            table.add_row([user['id'], user['name'], user['username'], user['email']])
        print(Fore.CYAN + "Список користувачів:" + Style.RESET_ALL)
        print(table)

    def display_user_posts(self, user_id):
        posts = self.user_repository.get_user_posts(user_id)
        table = PrettyTable()
        table.field_names = ["ID", "Title", "Body"]
        for post in posts:
            table.add_row([post['id'], post['title'], post['body']])
        print(Fore.GREEN + f"Пости користувача {user_id}:" + Style.RESET_ALL)
        print(table)

    def search_user_by_name(self, name):
        user = self.user_repository.get_user_by_name(name)
        if user:
            print(f"Користувач знайдений: {user}")
        else:
            print("Користувача з таким ім'ям не знайдено.")

    def display_history(self):
        print("Історія запитів:")
        for entry in self.history:
            print(entry)

    def save_data_to_file(self, data):
        """Метод для збереження даних у файли JSON, CSV або TXT"""
        print("Оберіть формат файлу для збереження:")
        print("1. JSON")
        print("2. CSV")
        print("3. TXT")
        choice = input("Введіть номер формату: ")

        if choice == "1":
            FileSaver.save_to_json(data)
        elif choice == "2":
            FileSaver.save_to_csv(data)
        elif choice == "3":
            FileSaver.save_to_txt(data)
        else:
            print("Неправильний вибір. Дані не збережено.")

    def menu(self):
        while True:
            print("\n" + Fore.YELLOW + "Меню:" + Style.RESET_ALL)
            print("1. Переглянути список користувачів")
            print("2. Переглянути пости користувача")
            print("3. Пошук користувача за іменем")
            print("4. Переглянути історію запитів")
            print("5. Зберегти дані")
            print("0. Вихід")

            choice = input("Оберіть дію: ")

            if choice == "1":
                # Отримуємо список користувачів з API
                users = self.user_repository.get_all_users()
                # Відображаємо список користувачів
                self.display_users()
                # Додаємо до історії
                self.history.append("Переглянуто список користувачів")
                # Зберігаємо отримані дані для подальшого збереження
                self.current_data = users

            elif choice == "2":
                user_id = input("Введіть ID користувача: ")
                if validate_entry(user_id):
                    # Отримуємо пости конкретного користувача
                    posts = self.user_repository.get_user_posts(int(user_id))
                    # Відображаємо пости
                    self.display_user_posts(int(user_id))
                    # Додаємо до історії
                    self.history.append(f"Переглянуто пости користувача {user_id}")
                    # Зберігаємо пости для подальшого збереження
                    self.current_data = posts
                else:
                    print("Некоректний ID користувача.")

            elif choice == "3":
                name = input("Введіть ім'я користувача для пошуку: ")
                # Пошук користувача за іменем
                user = self.user_repository.get_user_by_name(name)
                if user:
                    print(f"Користувач знайдений: {user}")
                    # Додаємо до історії
                    self.history.append(f"Пошук користувача з ім'ям {name}")
                    # Зберігаємо знайденого користувача для подальшого збереження
                    self.current_data = [user]  # Обгортаємо у список для узгодженості
                else:
                    print("Користувача з таким ім'ям не знайдено.")
                    self.current_data = None  # Скидаємо дані, якщо пошук не вдався

            elif choice == "4":
                # Відображення історії запитів
                self.display_history()

            elif choice == "5":
                # Збереження даних у файл
                if hasattr(self, 'current_data') and self.current_data:
                    self.save_data_to_file(self.current_data)
                else:
                    print("Немає даних для збереження. Спочатку перегляньте або отримайте дані.")

            elif choice == "0":
                print("Вихід із програми.")
                break

            else:
                print("Некоректний вибір. Спробуйте ще раз.")



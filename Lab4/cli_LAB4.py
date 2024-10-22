class CLI:

    #Введення користувача
    @staticmethod
    def get_user_input():
        return input("Введіть слово або фразу для перетворення в ASCII-арт: ")

    #Розміри ASCII-арту
    @staticmethod
    def get_art_dimensions():
        while True:
            try:
                width = int(input("Введіть ширину ASCII-арту (від 20 до 100): "))
                height = int(input("Введіть висоту ASCII-арту (від 5 до 20): "))
                if 20 <= width <= 100 and 5 <= height <= 20:
                    return width, height
                print("Розміри повинні бути в межах вказаного діапазону.")
            except ValueError:
                print("Будь ласка, введіть цілі числа.")

    @staticmethod
    def get_alignment():
        while True:
            alignment = input("Виберіть вирівнювання (left/center/right): ").lower()
            if alignment in ['left', 'center', 'right']:
                return alignment
            print("Будь ласка, виберіть коректне вирівнювання.")

    #Набір символів
    @staticmethod
    def get_custom_symbol():
        return input("Введіть символ для створення ASCII-арту (наприклад, '@', '#', '*'): ")

    #Варіанти кольорів
    @staticmethod
    def get_color_option():
        while True:
            color = input("Виберіть колірну схему (black_white/grayscale): ").lower()
            if color in ['black_white', 'grayscale']:
                return color
            print("Будь ласка, виберіть коректну колірну схему.")

    #Відображення мистецтва
    @staticmethod
    def display_art(art):
        for row in art:
            print(row)

    @staticmethod
    def get_save_choice():
        return input("Зберегти цей ASCII-арт? (y/n): ").lower() == 'y'

    @staticmethod
    def get_filename():
        return input("Введіть ім'я файлу для збереження: ")
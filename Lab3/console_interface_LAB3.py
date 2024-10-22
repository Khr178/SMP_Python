from BLL.art_generator_LAB3 import generate_ascii_art, generate_custom_symbol_art
from BLL.font_manager_LAB3 import get_available_fonts, is_valid_font
from BLL.color_manager_LAB3 import get_available_colors, is_valid_color
from DAL.file_handler_LAB3 import save_to_file
from Shared.utils_LAB3 import get_user_input


def start_console_interface():
    print("ASCII ART Генератор")

    # Введення тексту
    text = input("Введіть текст для ASCII-арту: ")

    # Вибір шрифту
    fonts = get_available_fonts()
    print("Доступні шрифти:", fonts[:20])  # Показуємо 20 перших шрифтів
    font = get_user_input("Виберіть шрифт: ", fonts)

    # Вибір кольору
    colors = get_available_colors()
    print("Доступні кольори:", colors)
    color = get_user_input("Виберіть колір: ", colors)

    # Введення ширини та висоти
    width = int(input("Введіть бажану ширину (наприклад, 100): "))
    height = input("Введіть бажану висоту: ") or None

    # Вибір символа для ASCII-арту
    use_custom_symbol = get_user_input("Використовувати кастомний символ замість '#' для ASCII-арту? (y/n): ",
                                       ['y', 'n'])
    if use_custom_symbol == 'y':
        symbol = input("Введіть символ, який буде використовуватися для заміни '#': ")
        ascii_art = generate_custom_symbol_art(text, font, width, symbol)
    else:
        ascii_art = generate_ascii_art(text, font, color, width=width, height=height)

    # Попередній перегляд ASCII-арту
    print("Попередній перегляд ASCII-арту:")
    print(ascii_art)

    # Збереження у файл
    save_choice = get_user_input("Зберегти результат у файл? (y/n): ", ['y', 'n'])
    if save_choice == 'y':
        filename = input("Введіть ім'я файлу: ")
        save_to_file(ascii_art, filename)
        print(f"ASCII-арт збережено у файл: assets/{filename}.txt")




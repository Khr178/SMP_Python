from UI.cli_LAB4 import CLI
from BLL.ascii_art_generator_LAB4 import ArtGenerator
from DAL.file_operations_LAB4 import FileManager
from Shared.utils2_LAB4 import align_text
from colorama import init

def run():
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

if __name__ == "__main__":
    run()

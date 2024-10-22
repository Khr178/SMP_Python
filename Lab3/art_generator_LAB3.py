import pyfiglet
from colorama import Fore, Style

# Доступні кольори з бібліотеки colorama
colors = {
    'red': Fore.RED,
    'green': Fore.GREEN,
    'blue': Fore.BLUE,
    'yellow': Fore.YELLOW,
    'magenta': Fore.MAGENTA,
    'cyan': Fore.CYAN,
    'white': Fore.WHITE
}

def generate_ascii_art(text, font, color, width=80, height=None):
    """Генерація ASCII-арту з використанням вибраного шрифту, кольору, ширини і висоти"""
    ascii_art = pyfiglet.figlet_format(text, font=font, width=width)
    color_code = colors.get(color.lower(), Fore.WHITE)  # Встановлюємо білий за замовчуванням
    colored_ascii_art = f"{color_code}{ascii_art}{Style.RESET_ALL}"
    return colored_ascii_art

def generate_custom_symbol_art(text, font, width, symbol):
    """Генерація ASCII-арту з кастомними символами"""
    ascii_art = pyfiglet.figlet_format(text, font=font, width=width)
    custom_art = ascii_art.replace('#', symbol)  # Замінюємо всі '#' на вибраний символ
    return custom_art







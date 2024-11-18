available_colors = ['red', 'green', 'blue', 'yellow', 'magenta', 'cyan', 'white']

def get_available_colors():
    """Отримання списку доступних кольорів"""
    return available_colors

def is_valid_color(color):
    """Перевірка, чи є колір у списку доступних"""
    return color in available_colors




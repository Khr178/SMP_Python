import pyfiglet

def get_available_fonts():
    """Отримання списку доступних шрифтів"""
    return pyfiglet.FigletFont.getFonts()

def is_valid_font(font):
    """Перевірка, чи шрифт існує в списку доступних"""
    return font in pyfiglet.FigletFont.getFonts()



import os

def save_to_file(content, filename):
    """Збереження ASCII-арту у файл"""
    if not os.path.exists('assets'):
        os.makedirs('assets')

    with open(f'assets/{filename}.txt', 'w') as file:
        file.write(content)


def load_from_file(filename):
    """Завантаження ASCII-арту з файлу"""
    with open(f'assets/{filename}.txt', 'r') as file:
        return file.read()


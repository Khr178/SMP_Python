from abc import ABC, abstractmethod


class MenuInterface(ABC):
    """Абстрактний базовий клас для реалізації меню"""

    @abstractmethod
    def show(self):
        """Відобразити меню"""
        pass

    @abstractmethod
    def add_item(self, name, function):
        """Додати пункт до меню"""
        pass
from colorama import Fore, Style
class Figure3D:
    @staticmethod
    def is_appropriate_character(character):
        return len(character) == 1

class Cube(Figure3D):
    def __init__(self, length, character, color_position):
        self.length = length
        self.character = character
        self.color_position = color_position

    def get_3d_representation(self, scale=1.0):
        l = int(self.length * scale)
        color = self.get_color()
        return [
            f"{color}    +{'-' * l}+{Style.RESET_ALL}",
            f"{color}  /{' ' * l}/ |{Style.RESET_ALL}",
            f"{color} +{'-' * l}+  +{Style.RESET_ALL}",
            f"{color} |{' ' * l}| /{Style.RESET_ALL}",
            f"{color} |{' ' * l}|/{Style.RESET_ALL}",
            f"{color} +{'-' * l}+{Style.RESET_ALL}"
        ]

    def get_2d_representation(self):
        color = self.get_color()
        return [
            f"{color}{self.character * self.length}{Style.RESET_ALL}",
            f"{color}{self.character}   {self.character}{Style.RESET_ALL}",
            f"{color}{self.character * self.length}{Style.RESET_ALL}"
        ]

    def get_color(self):
        colors = [Fore.RED, Fore.GREEN, Fore.BLUE]
        return colors[self.color_position]

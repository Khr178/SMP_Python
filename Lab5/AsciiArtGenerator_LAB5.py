from colorama import Back, Style

class AsciiArtGenerator:
    def add_shadow(self, ascii_art):
        shadow = []
        for line in ascii_art:
            shadow.append(Back.BLACK + line + Style.RESET_ALL)
        return ascii_art + [''] + shadow

    def add_lighting(self, ascii_art):
        lighting = []
        for line in ascii_art:
            lighting.append(Back.WHITE + line + Style.RESET_ALL)
        return lighting
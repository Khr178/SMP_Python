from Shared.utils2_LAB4 import base_font, align_text


class ArtGenerator:
    LETTERS = base_font()

#Функція генерації ASCII-арту
    @staticmethod
    def generate_art(text, width, height, custom_symbol, color_option):
        text = text.upper()
        letter_width = min(5, (width - len(text) + 1) // len(text))
        letter_height = min(5, height)
        art = [[' ' for _ in range(width)] for _ in range(height)]

        x_offset = 0
        for char in text:
            letter = ArtGenerator.LETTERS.get(char, ArtGenerator.LETTERS[' '])
            for y in range(letter_height):
                for x in range(letter_width):
                    if x + x_offset < width and y < height:
                        if letter[y][x] != ' ':
                            if color_option == 'black_white':
                                art[y][x + x_offset] = custom_symbol
                            else:  # grayscale
                                intensity = (x + y) % 4
                                art[y][x + x_offset] = ['░', '▒', '▓', '█'][intensity]
            x_offset += letter_width + 1
            if x_offset >= width:
                break

        return [''.join(row) for row in art]

    @staticmethod
    def _scale_letter(letter, width, height, custom_symbol, color_option):
        scaled = [[' ' for _ in range(width)] for _ in range(height)]
        orig_height, orig_width = len(letter), len(letter[0])

        for y in range(height):
            for x in range(width):
                orig_y = int(y * orig_height / height)
                orig_x = int(x * orig_width / width)
                if letter[orig_y][orig_x] != ' ':
                    if color_option == 'black_white':
                        scaled[y][x] = custom_symbol
                    else:  # grayscale
                        intensity = int((y * x * 25) / (height * width))
                        scaled[y][x] = chr(9617 + min(intensity // 8, 3))  # Unicode block elements

        return scaled
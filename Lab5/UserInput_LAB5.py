from classes.Shape3D_LAB5 import Figure3D


def get_character_input():
    while True:
        character = input("Enter a character to represent in the shape: ")
        if Figure3D.is_appropriate_character(character) is False:
            print("You should have entered one character!")
        else:
            return character

def get_color_position_input(colors):
    while True:
        try:
            color = int(input("Enter a number of color: "))
            if color not in range(len(colors)):
                print("You should have entered a color option which is available!")
            else:
                return color
        except ValueError:
            print("You should have entered an integer number!")

def get_length_input():
    while True:
        try:
            length = int(input("Enter a length: "))
            if length <= 0:
                print("You should have entered a length greater than 0!")
            else:
                return length
        except ValueError:
            print("You should have entered an integer number!")

def get_scale_input():
    while True:
        try:
            scale = float(input("Enter a scale for figure: "))
            if scale <= 0:
                print("You should have entered a scale greater than 0!")
            else:
                return scale
        except ValueError:
            print("You should have entered a float number!")
from classes.Shape3D_LAB5 import Cube
from BLL.AsciiArtGenerator_LAB5 import AsciiArtGenerator
from DAL.FileManager_LAB5 import FileManager
from Shared.UserInput_LAB5 import get_character_input, get_color_position_input, get_length_input, get_scale_input

def display_colors():
    colors = ["Red", "Green", "Blue"]
    for i, color in enumerate(colors):
        print(f"{i}: {color}")

def main():
    is_figure_available = False
    is_3d_representation_available = False
    representation_3d_file = "cube.txt"
    colors = ["Red", "Green", "Blue"]
    generator = AsciiArtGenerator()

    while True:
        print("1 - Create a cube")
        print("2 - Display 2D")
        print("3 - Save 3D")
        print("4 - Add Shadow")
        print("5 - Add Lighting")
        print("0 - Exit")
        option = str(input("Enter an option: "))

        match option:
            case "1":
                character = get_character_input()
                print("There are such colors available:")
                display_colors()
                color_position = get_color_position_input(colors)
                length = get_length_input()
                scale = get_scale_input()
                try:
                    figure = Cube(length, character, color_position)
                    is_figure_available = True
                    representation_3d = figure.get_3d_representation(scale=scale)
                    print("\n".join(representation_3d))
                    is_3d_representation_available = True
                except ValueError as e:
                    print(e)
                    is_figure_available = False
            case "2":
                if is_figure_available:
                    representation_2d = figure.get_2d_representation()
                    [print(item) for item in representation_2d]
                else:
                    print("There is no figure available!")
            case "3":
                if is_3d_representation_available:
                    FileManager.save_to_file(representation_3d_file, "\n".join(representation_3d))
                else:
                    print("There is no figure available!")
            case "4":
                if is_3d_representation_available:
                    shadow_art = generator.add_shadow(representation_3d)
                    print("\n".join(shadow_art))
                else:
                    print("There is no figure available!")
            case "5":
                if is_3d_representation_available:
                    lighting_art = generator.add_lighting(representation_3d)
                    print("\n".join(lighting_art))
                else:
                    print("There is no figure available!")
            case "0":
                break
            case _:
                print("Invalid option!")

if __name__ == "__main__":
    main()
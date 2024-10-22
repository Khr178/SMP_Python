class FileManager:
    @staticmethod
    def save_to_file(filename, content):
        try:
            with open(filename, "w") as file:
                file.write(content)
            print(f"Content saved to {filename}")
        except PermissionError:
            print("You do not have permission to write to the file!")
        except FileNotFoundError:
            print("The file does not exist!")
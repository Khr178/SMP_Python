class FileManager:
    #Збереження у файл
    @staticmethod
    def save_to_file(art, filename):
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                for row in art:
                    file.write(row + '\n')
            return True
        except IOError:
            return False

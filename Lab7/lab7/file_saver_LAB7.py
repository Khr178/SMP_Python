import json
import csv

class FileSaver:
    @staticmethod
    def save_to_json(data, filename="data.json"):
        """Зберігає дані у форматі JSON"""
        try:
            with open(filename, 'w', encoding='utf-8') as json_file:
                json.dump(data, json_file, ensure_ascii=False, indent=4)
                print(f"Дані збережено у файл {filename} у форматі JSON.")
        except Exception as e:
            print(f"Помилка при збереженні JSON: {e}")

    @staticmethod
    def save_to_csv(data, filename="data.csv"):
        """Зберігає дані у форматі CSV"""
        try:
            with open(filename, mode='w', newline='', encoding='utf-8') as csv_file:
                writer = csv.writer(csv_file)
                if isinstance(data, list) and all(isinstance(row, dict) for row in data):
                    headers = data[0].keys()
                    writer.writerow(headers)
                    for row in data:
                        writer.writerow(row.values())
                else:
                    writer.writerow(data)
            print(f"Дані збережено у файл {filename} у форматі CSV.")
        except Exception as e:
            print(f"Помилка при збереженні CSV: {e}")

    @staticmethod
    def save_to_txt(data, filename="data.txt"):
        """Зберігає дані у форматі TXT"""
        try:
            with open(filename, 'w', encoding='utf-8') as txt_file:
                if isinstance(data, list):
                    for item in data:
                        txt_file.write(f"{item}\n")
                else:
                    txt_file.write(str(data))
            print(f"Дані збережено у файл {filename} у форматі TXT.")
        except Exception as e:
            print(f"Помилка при збереженні TXT: {e}")
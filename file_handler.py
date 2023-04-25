import json
import os


class FileHandler:
    @staticmethod
    def write_to_file(file_name: str, dictionary: dict) -> None:
        name = f"{file_name}.json"
        if os.path.exists(name):
            file = open(name, "w", encoding="utf-8")

        json.dump(dictionary, file)
        print(f"Zapisano do pliku '{file_name}.json'")
        file.close()

    @staticmethod
    def read_file(file_name: str) -> None:
        try:
            file = open(file_name + ".json", "r", encoding="utf-8")
            dictionary = json.load(file)
            print(f"Odczytano dane z pliku '{file_name}.json'")
            file.close()
            return dictionary
        except FileNotFoundError:
            print("Plik o podanej nazwie nie istnieje.")

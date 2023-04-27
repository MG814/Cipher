import json
from buffer import Buffer


class FileHandler:
    @staticmethod
    def write_to_file(file_name: str, buffer: Buffer, extension: str = ".json") -> None:
        with open(f"{file_name}{extension}", "w", encoding="utf-8") as file:
            json.dump(buffer.data, file)

    @staticmethod
    def read_file(file_name: str, extension: str = ".json") -> list[dict]:
        try:
            with open(f"{file_name}{extension}", "r", encoding="utf-8") as file:
                data_list = json.load(file)
            return data_list
        except FileNotFoundError:
            print("Plik o podanej nazwie nie istnieje.")

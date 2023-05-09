import os
import json
from dataclasses import asdict

from buffer import Buffer


class FileHandler:
    @staticmethod
    def write_to_file(file_name: str, buffer: Buffer, extension: str = ".json") -> None:
        with open(f"{file_name}{extension}", "w", encoding="utf-8") as file:
            dict_list = [asdict(text_obj) for text_obj in buffer.data]
            json.dump(dict_list, file)

    @staticmethod
    def read_file(file_name: str, extension: str = ".json") -> list[dict]:
        try:
            with open(f"{file_name}{extension}", "r", encoding="utf-8") as file:
                data_list = json.load(file)
            return data_list
        except FileNotFoundError:
            print("Plik o podanej nazwie nie istnieje.")

    @staticmethod
    def file_exists(file_name: str, extension: str = ".json") -> bool:
        if os.path.exists(f"{file_name}{extension}"):
            return True
        return False

    @staticmethod
    def enter_file_name() -> str:
        file_name = input("Podaj nazwę pliku:\n")
        return file_name

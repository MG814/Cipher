import sys

from file_handler import FileHandler
from manager import Manager


class Menu:
    def __init__(self):
        self.file_handler = FileHandler()
        self.manager = Manager()
        self.type_rot = ""
        self.options = {
            1: {
                1: self.type_cipher_menu,
                2: self.manager.write,
                3: self.decryption_menu,
            },
            2: {1: "rot13", 2: "rot47"},
            3: {1: self.manager.cesar_decrypted, 2: self.manager.buffer.data},
        }

    def type_cipher_menu(self) -> None:
        self.manager.enter_string()

        choice = int(input("Wybierz rodzaj szyfru:\n1 - rot13\n2 - rot47\n"))
        self.type_menu_execute(choice)

        self.manager.cesar_encrypted(self.type_rot)
        self.manager.add_to_buffer()
        print(self.manager.buffer.data)

    def main_menu(self) -> None:
        choice = int(
            input(
                "\nMenu główne:\n1 - Zaszyfruj tekst\n2 - Zapis do pliku\n3 - Odczyt z pliku\n4 - Wyjdź\n"
            )
        )
        self.execute(choice)

    def decryption_menu(self) -> None:
        self.manager.read_to_buffer()
        choice = int(
            input("Czy chcesz odszyfrować zawartość pliku?\n1 - Tak\n2 - Nie\n")
        )
        self.decryption_menu_execute(choice)

    def execute(self, choice: int) -> None:
        if choice in range(1, 4, 1):
            self.options.get(1).get(choice)()
        elif choice == 4:
            sys.exit(0)

    def type_menu_execute(self, choice: int) -> None:
        self.type_rot = self.options.get(2).get(choice)

    def decryption_menu_execute(self, choice: int) -> None:
        self.options.get(3).get(choice)()

import sys

from buffer import Buffer, Text
from cesar_cipher import Rot
from file_handler import FileHandler
from menu import Menu


class Manager:
    def __init__(self):
        self.menu = Menu()
        self.cesar_cipher = Rot()
        self.buffer = Buffer()
        self.rot_type: str = ""
        self.string: str = ""
        self.options = {
            1: {
                1: self.type_cipher_menu,
                2: self.write,
                3: self.decryption_menu,
            },
            2: {1: "rot13", 2: "rot47"},
            3: {1: self.cesar_decrypted, 2: self.buffer.data},
        }

    def enter_string(self) -> str:
        text = input("Podaj swój tekst:\n")
        self.string = text
        return text

    def write(self) -> None:
        file_name = FileHandler.enter_file_name()
        if FileHandler.file_exists(file_name):
            self.add_to_buffer_datafile(file_name)
        FileHandler.write_to_file(file_name, self.buffer)
        print(f"Zapisano do pliku '{file_name}'")

    def read_to_buffer(self) -> None:
        self.buffer.clear_buffer()
        file_name = FileHandler.enter_file_name()
        self.add_to_buffer_datafile(file_name)
        print(f"Odczytano dane z pliku '{file_name}'")

    def add_to_buffer_datafile(self, file_name: str) -> None:
        file_data_list = FileHandler.read_file(file_name)
        for f_dict in file_data_list:
            self.buffer.add_data(Text(**f_dict))

    def cesar_encrypted(self, new_rot_type: str) -> str:
        encryption_string = Rot.create_rot(new_rot_type).encrypt_decrypt(
            self.string, "encrypted"
        )

        self.string = encryption_string

        print(f"Zaszyfrowano szyfrem typu {new_rot_type}")
        return encryption_string

    def cesar_decrypted(self) -> list[Text]:
        for text in self.buffer.data:
            self.cesar_decrypted_buffer(text)
        print(f"\n{self.buffer.data}")
        print(f"Odzszyfrowano dane.")
        return self.buffer.data

    def cesar_decrypted_buffer(self, buffer_dict: Text) -> None:
        rot_type = buffer_dict.rot_type

        buffer_dict.text = Rot.create_rot(rot_type).encrypt_decrypt(
            buffer_dict.text, "decrypted"
        )

        buffer_dict.status = "decrypted"

    def add_to_buffer(self) -> None:
        self.buffer.add_data(Text(self.string, "encrypted", self.rot_type))

    def main_menu(self) -> None:
        try:
            choice = self.menu.show_main_menu()
            self.execute(choice)
        except ValueError:
            print("Podana wartość nie jest liczbą całkowitą.")

    def execute(self, choice: int) -> None:
        if choice in range(1, len(self.options[1]) + 1, 1):
            self.options.get(1).get(choice)()
        elif choice == 4:
            sys.exit(0)

    def type_cipher_menu(self) -> None:
        try:
            self.enter_string()
            self.buffer.clear_buffer()

            choice = self.menu.show_type_cipher_menu()
            self.type_menu_execute(choice)

            encrypted_str = self.cesar_encrypted(self.rot_type)

            self.buffer.add_data(Text(encrypted_str, "encrypted", self.rot_type))
            print(self.buffer.data)
        except ValueError:
            print("Podana wartość nie jest liczbą całkowitą.")
        except AttributeError:
            print("Nie wybrano typu szyfrowania.")

    def type_menu_execute(self, choice: int) -> None:
        self.rot_type = self.options.get(2).get(choice)

    def decryption_menu(self) -> None:
        try:
            choice = self.menu.show_decryption_menu()
            self.read_to_buffer()
            self.decryption_menu_execute(choice)
            self.buffer.clear_buffer()
        except ValueError:
            print("Podana wartość nie jest liczbą całkowitą.")

    def decryption_menu_execute(self, choice: int) -> None:
        if choice == 1:
            self.options.get(3).get(choice)()
        elif choice == 2:
            print(self.options.get(3).get(choice))

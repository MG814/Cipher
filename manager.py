from buffer import Buffer, Text
from cesar_cipher import Rot
from file_handler import FileHandler


class Manager:
    def __init__(self):
        self.file_handler = FileHandler()
        self.cesar_cipher = Rot()
        self.buffer = Buffer()
        self.rot_type = ""
        self.string = ""

    def enter_file_name(self) -> str:
        file_name = input("Podaj nazwę pliku:\n")
        return file_name

    def enter_string(self) -> str:
        text = input("Podaj swój tekst:\n")
        self.string = text
        return text

    def write(self) -> None:
        file_name = self.enter_file_name()
        self.file_handler.write_to_file(file_name, self.buffer)

    def read(self):  # FIXME read_to_buffer.
        file_name = self.enter_file_name()
        my_list = self.file_handler.read_file(file_name)
        for item in my_list:
            self.buffer.add_data(item)

    def cesar_encrypted(self, new_rot_type="") -> str:
        self.rot_type = new_rot_type
        encryption_string = Rot.create_rot(new_rot_type).rot_encryption(self.string)
        self.string = encryption_string
        print(f"Zaszyfrowano szyfrem typu {self.rot_type}")
        return encryption_string

    def cesar_decrypted(self) -> list[dict]:
        for idx, text in enumerate(self.buffer.data):
            decryption_string = Rot.create_rot(text.get("rot_type")).rot_decryption(
                text.get("text")
            )
            self.buffer.data[idx]["text"] = decryption_string
            self.buffer.data[idx]["status"] = "decrypted"
        print(self.buffer.data)
        print(f"Odzszyfrowano dane.")
        return self.buffer.data

    def add_to_buffer(self):
        self.buffer.add_data(Text(self.string, "encrypted", self.rot_type).for_json())

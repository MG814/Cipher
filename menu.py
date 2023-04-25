import os

from FileHandler import FileHandler
from cesar_cipher import CesarCipher


class Menu:
    def show_menu(self):
        print("1 - Zapis do pliku\n2 - Odczyt z pliku\n3 - Wyjdź")

    def show_sub_menu(self, choice1: str, choice2: str):
        print(f"1 - {choice1}\n2 - {choice2}")

    def get_choice(self, min: int, max: int):
        choice = int(input("Podaj odpowiednią cyfrę:\n"))

        if min > choice or choice > max:
            raise WrongNumber
        elif choice == "w":
            raise ValueError("Proszę wybrać jedną z liczb podanych w menu.")
        return choice

    def menu_logic(self):
        file_name = input("Podaj nazwę pliku:\n")
        file_handler = FileHandler(file_name)
        cipher = CesarCipher()
        if os.path.exists(file_name + ".json"):
            my_id = len(file_handler.read_file()) + 1
            dict_buffer = file_handler.read_file()
        else:
            my_id = 1
            dict_buffer = {}
        while True:
            self.show_menu()
            try:
                choice = self.get_choice(1, 3)
                if choice == 1:
                    dict = {}
                    text = input("Text:\n")
                    self.show_sub_menu("Szyfrowanie rot13", "Szyfrowanie rot47")  # źle
                    sub_choice = self.get_choice(1, 2)

                    if sub_choice == 1:
                        dict["text"] = cipher.rot13(text)
                        dict["status"] = "encrypted"
                        dict["rot_type"] = "rot13"
                    else:
                        dict["text"] = cipher.rot47(text)
                        dict["status"] = "encrypted"
                        dict["rot_type"] = "rot47"

                    dict_buffer[my_id] = dict
                    my_id += 1
                    file_handler.write_to_file(dict_buffer)
                elif choice == 2:
                    self.show_sub_menu("Dane odszyfrowane", "Dane zaszyfrowane")
                    sub_choice = self.get_choice(1, 2)

                    if sub_choice == 1:
                        dict = {}
                        dict_buffer = file_handler.read_file()
                        for k, v in file_handler.read_file().items():
                            print(k)
                            for key in v:
                                if key == "text":
                                    if v["rot_type"] == "rot13":
                                        dict[key] = cipher.decryption_rot13(v[key])
                                    elif v["rot_type"] == "rot47":
                                        dict[key] = cipher.decryption_rot47(v[key])
                                    print(dict[key])
                                    dict_buffer[k][key] = dict[key]
                                    dict_buffer[k]["status"] = "decrypted"
                        print(dict_buffer)
                    elif sub_choice == 2:
                        print(file_handler.read_file())
                elif choice == 3:
                    break
            except (WrongNumber, ValueError) as e:
                print(e)

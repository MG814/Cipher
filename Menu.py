from FileHandler import FileHandler


class WrongNumber(Exception):
    def __str__(self):
        return "Podana liczba jest poza przedziałem."


class Menu:
    def show_menu(self):
        print("1 - Zapis do pliku\n2 - Odczyt z pliku\n3 - Wyjdź")

    def get_choice(self):
        choice = int(input("Podaj odpowiednią cyfrę:\n"))

        if 1 > choice or choice > 3:
            raise WrongNumber
        elif choice == "w":
            raise ValueError("Proszę wybrać jedną z liczb podanych w menu głównym.")
        return choice

    def menu_logic(self):
        file_name = input("Podaj nazwę pliku:\n")
        file_handler = FileHandler(file_name)
        dict_buffer = {"klucz1": "wartosc1", "klucz2": "wartosc2"}
        while True:
            self.show_menu()
            try:
                choice = self.get_choice()
                if choice == 1:
                    file_handler.write_to_file(dict_buffer)
                elif choice == 2:
                    print(file_handler.read_file())
                elif choice == 3:
                    break
                else:
                    break
            except (WrongNumber, ValueError) as e:
                print(e)

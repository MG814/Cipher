class Menu:
    def show_main_menu(self) -> int:
        choice = int(
            input(
                "\nMenu główne:\n1 - Zaszyfruj tekst\n2 - Zapis do pliku\n3 - Odczyt z pliku\n4 - Wyjdź\n"
            )
        )
        return choice

    def show_type_cipher_menu(self) -> int:
        choice = int(input("\nWybierz rodzaj szyfru:\n1 - rot13\n2 - rot47\n"))
        return choice

    def show_decryption_menu(self) -> int:
        choice = int(
            input("\nCzy chcesz odszyfrować zawartość pliku?\n1 - Tak\n2 - Nie\n")
        )
        return choice

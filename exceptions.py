class WrongNumber(Exception):
    def __str__(self):
        return "Podana liczba jest poza przedziałem."

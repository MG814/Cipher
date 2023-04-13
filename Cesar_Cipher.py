import string
from abc import ABC, abstractmethod


class Rot(ABC):
    pass


class Rot13(Rot):
    pass


class Rot47(Rot):
    pass


class CesarCipher:
    def rot13(self, text: str):
        abc = "aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż"
        return (lambda y: "".join([abc[(abc.find(x) + 13) % 35] for x in y]))(text)

    def decryption_rot13(self, text: str):
        abc = "aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż"
        return (lambda y: "".join([abc[(abc.find(x) - 13) % 35] for x in y]))(text)

    def rot47(self, text: str):
        new = ""
        for x in text:
            if 33 <= ord(x) <= 126:
                new += chr((ord(x) + 47) % 94)
        return new

    def decryption_rot47(self, text: str):
        new = ""
        for x in text:
            if 33 <= ord(x) <= 126:
                new += chr((ord(x) - 47) % 94)
        return new

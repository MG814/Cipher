import string
from abc import ABC


class Rot(ABC):
    def rot_encryption(self, text: str):
        raise NotImplementedError

    def rot_decryption(self, text: str):
        raise NotImplementedError

    @staticmethod
    def create_rot(rot_type):
        rot_types = {"rot13": Rot13(), "rot47": Rot47()}
        return rot_types.get(rot_type)


class Rot13(Rot):
    def rot_encryption(self, text: str):
        abc = string.ascii_letters
        return (lambda y: "".join([abc[(abc.find(x) + 13) % 35] for x in y]))(text)

    def rot_decryption(self, text: str):
        abc = string.ascii_letters
        return (lambda y: "".join([abc[(abc.find(x) - 13) % 35] for x in y]))(text)


class Rot47(Rot):
    def rot_encryption(self, text: str):
        new = ""
        for x in text:
            if 33 <= ord(x) <= 126:
                new += chr((ord(x) + 47) % 94)
        return new

    def rot_decryption(self, text: str):
        new = ""
        for x in text:
            if 33 <= ord(x) <= 126:
                new += chr((ord(x) - 47) % 94)
        return new

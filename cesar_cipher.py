import string
from abc import ABC


class AvailableRot:
    ROT13 = "rot13"
    ROT47 = "rot47"


class Rot(ABC):
    def encrypt_decrypt(self, text: str, direction: str):
        raise NotImplementedError

    @staticmethod
    def create_rot(rot_type):
        rot_types = {"rot13": Rot13(), "rot47": Rot47()}
        return rot_types.get(rot_type)


class Rot13(Rot):
    def encrypt_decrypt(self, text: str, direction: str) -> str:
        abc = string.ascii_letters
        shift = 13 if direction == "encrypted" else -13
        return (lambda y: "".join([abc[(abc.find(x) + shift) % 52] for x in y]))(text)


class Rot47(Rot):
    def encrypt_decrypt(self, text: str, direction: str) -> str:
        new = ""
        for x in text:
            if 33 <= ord(x) <= 126:
                new += chr(33 + ((ord(x) + 14) % 94))
        return new

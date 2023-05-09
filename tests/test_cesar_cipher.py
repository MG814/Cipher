import pytest
from cesar_cipher import Rot13, Rot47, Rot


class TestCesarCipher:
    @pytest.mark.parametrize(
        "word, result", [("Ala", "Nyn"), ("pieczarki", "CvrpMnExv")]
    )
    def test_encryption_rot13(self, word, result):
        direction = "encrypted"
        rot13 = Rot13()

        assert rot13.encrypt_decrypt(word, direction) == result

    def test_decryption_rot13(self):
        text = "Nyn"
        direction = "decrypted"
        rot13 = Rot13()

        assert rot13.encrypt_decrypt(text, direction) == "Ala"

    def test_encryption_rot47(self):
        text = "Ala"
        direction = "encrypted"
        rot47 = Rot47()

        assert rot47.encrypt_decrypt(text, direction) == "p=2"

    def test_decryption_rot47(self):
        text = "p=2"
        direction = "encrypted"
        rot47 = Rot47()

        assert rot47.encrypt_decrypt(text, direction) == "Ala"

    @pytest.mark.parametrize("rot_type, rot_obj", [("rot13", Rot13), ("rot47", Rot47)])
    def test_create_rot_method(self, rot_type, rot_obj):
        assert isinstance(Rot.create_rot(rot_type), rot_obj)

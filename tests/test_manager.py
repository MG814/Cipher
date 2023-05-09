from unittest.mock import patch

from buffer import Text
from manager import Manager


class TestManager:
    def setup_method(self):
        self.manager = Manager()

    def test_enter_string_method(self):
        with patch("builtins.input", return_value="random_string"):
            assert self.manager.enter_string() == "random_string"

    def test_cesar_decrypted_buffer_method_change_status_in_text_object(self):
        self.text = Text("ddsf", "encrypted", "rot13")
        self.manager.cesar_decrypted_buffer(self.text)
        assert self.text.status == "decrypted"

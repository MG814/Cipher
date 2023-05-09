from unittest.mock import patch
import os

from buffer import Text, Buffer
from file_handler import FileHandler
import tempfile


def get_file_patch(file_name: str = "file.json") -> str:
    file_path = ""
    for root, dir, files in os.walk(os.getcwd()[:2]):
        if file_name in files:
            file_path = os.path.join(root, file_name)
    return file_path


def data_file():
    dict_list = FileHandler.read_file(get_file_patch(), "")
    return dict_list


class TestFileHandler:
    def test_enter_file_name_method(self):
        with patch("builtins.input", return_value="random_file"):
            assert FileHandler.enter_file_name() == "random_file"

    def test_file_exists_method_return_false(self):
        assert not FileHandler.file_exists("plik2")

    def test_file_exist_method_return_true(self):
        with tempfile.NamedTemporaryFile(suffix=".json", delete=True) as f:
            assert FileHandler.file_exists(f.name, extension="")

    def test_read_file_method_return_list(self):
        assert isinstance(data_file(), list)

    def test_read_file_method_elements_on_list_are_dict_type(self):
        for dictionary in data_file():
            assert isinstance(dictionary, dict)

    def test_write_to_file_method(self):
        self.text = Text("ddsf", "encrypted", "rot13")
        self.buffer = Buffer()
        self.buffer.add_data(self.text)
        FileHandler.write_to_file("my_file", self.buffer)
        for dictionary in FileHandler.read_file("my_file"):
            assert Text(**dictionary) == self.text

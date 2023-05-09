from dataclasses import dataclass
from typing import List


@dataclass
class Text:
    text: str
    status: str
    rot_type: str


class Buffer:
    _data: List[Text] = []

    def add_data(self, item: Text) -> None:
        self._data.append(item)

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    def clear_buffer(self) -> None:
        self._data.clear()

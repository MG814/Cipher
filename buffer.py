from dataclasses import dataclass, asdict
from typing import List


@dataclass
class Text:
    text: str
    status: str
    rot_type: str

    def for_json(self) -> dict:
        return asdict(self)

    # def __repr__(self):
    #     pass


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

    def clear_buffer(self):
        self._data.clear()

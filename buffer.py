from dataclasses import dataclass, asdict
from typing import List


@dataclass
class Text:
    text: str
    status: str
    rot_type: str

    def for_json(self) -> dict:
        return asdict(self)


class Buffer:
    _data: List[dict] = []

    def add_data(self, d: dict) -> None:
        self._data.append(d)

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

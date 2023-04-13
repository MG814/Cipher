from typing import List
from dataclasses import dataclass, asdict


class Text:
    text: str
    status: str
    rot_type: str

    def __str__(self):
        return ""


class Buffer:
    _data: List[Text] = []

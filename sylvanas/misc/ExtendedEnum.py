from enum import IntEnum, Enum
from random import choice
from typing import List


class ExtendedIntEnum(IntEnum):

    @classmethod
    def toArray(cls) -> List[int]:
        return list(map(lambda c: c.value, cls))

    @classmethod
    def randomize(cls) -> int:
        return choice(cls.toArray())


class ExtendedStringEnum(Enum):

    @classmethod
    def toArray(cls) -> List[str]:
        return [e.value for e in cls]

import string
from abc import ABC
from random import choice


class RandomUtils(ABC):

    @staticmethod
    def generateString(size: int):
        return ''.join(choice(string.ascii_uppercase + string.digits) for _ in range(size))

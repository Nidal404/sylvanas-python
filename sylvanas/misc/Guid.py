import uuid
from abc import ABC


class Guid(ABC):

    @staticmethod
    def new() -> str:
        return str(uuid.uuid4())

from abc import ABC, abstractmethod

from sylvanas.database.Entity import Entity


class EntityFactory(ABC):

    @staticmethod
    @abstractmethod
    def create(**kwargs) -> Entity:
        raise NotImplementedError()

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional

from sylvanas.Handler import Handler
from sylvanas.database.Entity import Entity

# Define a generic type for the entity
T = TypeVar('T', bound=Entity)


class UpsertHandler(Generic[T], Handler, ABC):

    @abstractmethod
    def createNewItem(self) -> T:
        raise NotImplementedError()

    @abstractmethod
    def updateItem(self, item: T):
        raise NotImplementedError()

    @abstractmethod
    def getEntity(self, entityId: str) -> Optional[T]:
        raise NotImplementedError()

    def handle(self, **kwargs):
        entity: T = self.getEntity(self.getAttribute('id'))
        if entity is None:
            entity = self.createNewItem()
            self.dbSession.add(entity)
        else:
            self.updateItem(entity)

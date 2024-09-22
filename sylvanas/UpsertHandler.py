from abc import ABC, abstractmethod
from typing import Optional

from sylvanas.Handler import Handler
from sylvanas.database.Entity import Entity


class UpsertHandler(Handler, ABC):

    @abstractmethod
    def createNewItem(self) -> Entity:
        raise NotImplementedError()

    @abstractmethod
    def updateItem(self, item: Entity):
        raise NotImplementedError()

    @abstractmethod
    def getEntity(self, entityId: str) -> Optional[Entity]:
        raise NotImplementedError()

    def handle(self, **kwargs):
        entity: Entity = self.getEntity(self.getAttribute('id', silent=False))

        if entity is None:
            entity = self.createNewItem()
            self.dbSession.add(entity)
        else:
            self.updateItem(entity)

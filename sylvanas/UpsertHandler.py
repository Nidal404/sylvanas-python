from abc import ABC, abstractmethod
from typing import Optional

from sylvanas.Handler import Handler
from sylvanas.database.Entity import Entity


class UpsertHandler(Handler, ABC):

    @abstractmethod
    def addNewEntity(self) -> Entity:
        raise NotImplementedError()

    @abstractmethod
    def updateEntity(self, item: Entity):
        raise NotImplementedError()

    @abstractmethod
    def getEntity(self, entityId: str) -> Optional[Entity]:
        raise NotImplementedError()

    def handle(self, **kwargs):
        entity: Entity = self.getEntity(self.getAttribute('id', silent=False))

        if entity is None:
            entity = self.addNewEntity()
            self.dbSession.add(entity)
        else:
            self.updateEntity(entity)

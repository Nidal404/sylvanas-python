from abc import ABC, abstractmethod
from typing import Dict

from sqlalchemy.orm import Session

from sylvanas.Utils.DateUtils import DateUtils


class Handler(ABC):

    @abstractmethod
    def defineSchema(self):
        raise NotImplementedError()

    @abstractmethod
    def handle(self, **kwargs):
        raise NotImplementedError()

    def __init__(self, dbSession: Session, body: Dict):
        if not isinstance(dbSession, Session):
            raise TypeError('DbSession must be type of Session')

        self.dbSession = dbSession
        self.body: Dict = body
        self.now = DateUtils.UtcNow()

    def getAttribute(self, key: str, silent: bool = True):
        if key not in self.body and not silent:
            raise AttributeError(f'{key} not found')
        return self.body.get(key)

    def getUserId(self) -> str:
        return self.getAttribute('user_id')

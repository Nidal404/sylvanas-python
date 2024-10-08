from abc import ABC, abstractmethod
from typing import Dict

from sqlalchemy.orm import Session

from sylvanas.Exceptions import ArgumentException
from sylvanas.HandlerLogger import HandlerLogger
from sylvanas.misc.JsonSchemaValidator import JsonSchemaValidator
from sylvanas.utils.DateUtils import DateUtils


class HandlerBase(ABC):

    def __init__(self, dbSession: Session):
        if not isinstance(dbSession, Session):
            raise TypeError('DbSession must be type of Session')

        self.dbSession = dbSession
        self.now = DateUtils.UtcNow()


class Handler(HandlerBase, ABC):

    @abstractmethod
    def defineSchema(self):
        raise NotImplementedError()

    @abstractmethod
    def handle(self, **kwargs):
        raise NotImplementedError()

    def response(self, **kwargs):
        pass

    def __init__(self, dbSession: Session, body: Dict):
        super().__init__(dbSession)

        if not isinstance(body, dict):
            raise TypeError('Body format is not valid, dict expected')

        self.validateSchema(body)  # Will raise
        self.body: Dict = body
        self.logger = HandlerLogger(self.dbSession, self.__class__.__name__, body)

    def validateSchema(self, body: Dict):
        schema = self.defineSchema()
        if not isinstance(schema, dict):
            raise TypeError('Schema format is not valid, dict expected')

        errors = JsonSchemaValidator(schema, body).validate()
        if len(errors) > 0:
            raise ArgumentException(errors)

    def getAttribute(self, key: str, silent: bool = True):
        if key not in self.body and not silent:
            raise AttributeError(f'{key} not found')
        return self.body.get(key)

    def isAttributeExists(self, key: str) -> bool:
        return key in self.body

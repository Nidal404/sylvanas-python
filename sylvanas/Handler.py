from abc import ABC, abstractmethod
from typing import Dict

from sqlalchemy.orm import Session

from sylvanas.Exceptions import ArgumentException
from sylvanas.Utils.DateUtils import DateUtils
from sylvanas.misc.JsonSchemaValidator import JsonSchemaValidator


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
        if not isinstance(body, dict):
            raise TypeError('Body format is not valid, dict expected')

        self.validateSchema(body)  # Will raise

        self.dbSession = dbSession
        self.body: Dict = body
        self.now = DateUtils.UtcNow()

    def validateSchema(self, body: Dict):
        schema = self.defineSchema()
        if not isinstance(schema, dict):
            raise TypeError('Schema format is not valid, dict expected')

        errors = JsonSchemaValidator(schema, body).validate()
        if len(errors):
            raise ArgumentException("Invalid json", errors)

    def getAttribute(self, key: str, silent: bool = True):
        if key not in self.body and not silent:
            raise AttributeError(f'{key} not found')
        return self.body.get(key)

    def getUserId(self) -> str:
        return self.getAttribute('user_id')

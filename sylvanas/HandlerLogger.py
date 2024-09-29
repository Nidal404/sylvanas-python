import traceback
from typing import Dict

from sqlalchemy.orm import Session

from sylvanas.Enums import HandlerLoggerSeverityLevel
from sylvanas.Exceptions import DevException
from sylvanas.database.Entities import HandlerLog
from sylvanas.misc.Guid import Guid
from sylvanas.utils.DateUtils import DateUtils
from sylvanas.utils.ValidationUtils import ValidationUtils


class HandlerLogger:

    def __init__(self, dbSession: Session, handlerName: str, payload: Dict):
        if not isinstance(dbSession, Session):
            raise TypeError('DbSession must be type of Session')

        self._dbSession = dbSession
        self._handlerName: str = handlerName
        self._payload = str(payload)
        self._log: HandlerLog = self._prepareLog()

    def _prepareLog(self) -> HandlerLog:
        log = HandlerLog()
        log.id = Guid.new()
        log.created_datetime = DateUtils.UtcNow()
        log.handler_name = self._handlerName
        log.severity_level = None
        log.message = ''
        log.payload = self._payload
        log.additional_properties = ''
        log.error = ''
        log.error_trace = ''

        return log

    def _setSeverityLevel(self, level: HandlerLoggerSeverityLevel):
        if self._log.severity_level is not None:
            raise DevException('Cannot set severityLevel multiple times')

        self._log.severity_level = level.value

    def trace(self, forceRollbackAndCommit: bool = False):
        if self._log.severity_level is None or self._log.severity_level not in HandlerLoggerSeverityLevel.toArray():
            raise DevException('SeverityLevel must be set by calling "info", "warning" or "error" method')
        if ValidationUtils.isStrNullOrEmpty(self._log.handler_name):
            raise DevException('HandlerName must be set')

        try:
            if forceRollbackAndCommit:
                self._dbSession.rollback()
                self._dbSession.add(self._log)
                self._dbSession.commit()
            else:
                self._dbSession.add(self._log)
        except Exception as e:
            print({str(e)})

        self._log = self._prepareLog()  # On reset les info du log

    def info(self):
        self._setSeverityLevel(HandlerLoggerSeverityLevel.INFO)
        return self

    def warning(self):
        self._setSeverityLevel(HandlerLoggerSeverityLevel.WARNING)
        return self

    def exception(self, e: BaseException):
        if not isinstance(e, BaseException):
            raise TypeError('e must be an Exception')

        self._setSeverityLevel(HandlerLoggerSeverityLevel.ERROR)
        self._log.error = e.__class__.__name__
        self._log.error_trace = traceback.format_exc()

        return self

    def withAdditionalProperties(self, additionalProperties: Dict):
        if not isinstance(additionalProperties, dict):
            raise TypeError('AdditionalProperties must be a dictionary')

        self._log.additional_properties = str(additionalProperties)
        return self

    def withMessage(self, message: str):
        if ValidationUtils.isStrNullOrEmpty(message):
            raise TypeError('Message must be set')

        self._log.message = message.strip()
        return self

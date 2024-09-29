from sylvanas.Enums import HandlerLoggerSeverityLevel
from sylvanas.Handler import Handler
from sylvanas.database.Database import dbSessionScope, Database
from sylvanas.database.Entities import HandlerLog
from sylvanas.misc.Assert import Assert
from sylvanas.misc.Guid import Guid
from unittests.config.BaseTest import HandlerBaseTest


class CustomCommandHandler(Handler):
    def defineSchema(self):
        return {
            "type": "object",
            "trim": ["user_id"],
            "required": ["user_id"],
            "properties": {
                "user_id": {"type": "string", "minLength": 36, "maxLength": 36},
            }
        }

    def handle(self, **kwargs):
        """
        Trois logs doivent être créés
        """
        self.logger.info().withMessage("coucou").trace()
        self.logger.warning().withAdditionalProperties({'name': 'Marco'}).trace()

        try:
            raise ValueError("Sylvanas error value")
        except ValueError as e:
            self.logger.exception(e).trace()

    def handleWithForceCommit(self):
        """
        Un seul log sera créé à cause du forceRollbackAndCommit
        """
        self.logger.info().withMessage("coucou").trace()  # Non pris en compte

        try:
            raise ValueError("Sylvanas error value")
        except ValueError as e:
            self.logger.exception(e).trace(forceRollbackAndCommit=True)


class TestHandlerLogger(HandlerBaseTest):
    HANDLER = CustomCommandHandler

    def test_HandlerLogger(self):
        body = {'user_id': Guid.new()}

        self.runHandler(body)
        Assert.areEqual(3, self.dbSession.query(HandlerLog).count())

        def AssertHandlerLogInfo():
            handlerLog = self.dbSession.query(HandlerLog) \
                .where(HandlerLog.severity_level == HandlerLoggerSeverityLevel.INFO) \
                .one()

            Assert.areEntityPropertiesEqual(handlerLog, {
                'handler_name': CustomCommandHandler.__name__,
                'severity_level': HandlerLoggerSeverityLevel.INFO.value,
                'message': 'coucou',
                'payload': str(body),
                'additional_properties': '',
                'error': '',
                'error_trace': '',
            })

        def AssertHandlerLogWarning():
            handlerLog = self.dbSession.query(HandlerLog) \
                .where(HandlerLog.severity_level == HandlerLoggerSeverityLevel.WARNING) \
                .one()

            Assert.areEntityPropertiesEqual(handlerLog, {
                'handler_name': CustomCommandHandler.__name__,
                'severity_level': HandlerLoggerSeverityLevel.WARNING.value,
                'message': '',
                'payload': str(body),
                'additional_properties': str({'name': 'Marco'}),
                'error': '',
                'error_trace': '',
            })

        def AssertHandlerLogError():
            handlerLog = self.dbSession.query(HandlerLog) \
                .where(HandlerLog.severity_level == HandlerLoggerSeverityLevel.ERROR) \
                .one()

            Assert.areEntityPropertiesEqual(handlerLog, {
                'handler_name': CustomCommandHandler.__name__,
                'severity_level': HandlerLoggerSeverityLevel.ERROR.value,
                'message': '',
                'payload': str(body),
                'additional_properties': '',
                'error': ValueError.__name__,
                'error_trace': lambda x: 'Sylvanas error value' in x,
            })

        AssertHandlerLogInfo()
        AssertHandlerLogWarning()
        AssertHandlerLogError()

    def test_HandlerLoggerWithForceCommit(self):
        body = {'user_id': Guid.new()}

        with (dbSessionScope(Database(self._engine).openDbSession()) as dbSession):
            handler = self.HANDLER(dbSession, body)
            handler.handleWithForceCommit()

        Assert.areEqual(1, self.dbSession.query(HandlerLog).count())

        # HandlerLog
        def AssertHandlerLog():
            handlerLog = self.dbSession.query(HandlerLog).one()
            Assert.areEntityPropertyCountEqual(9, handlerLog)
            Assert.areEntityPropertiesEqual(handlerLog, {
                'handler_name': CustomCommandHandler.__name__,
                'severity_level': HandlerLoggerSeverityLevel.ERROR.value,
                'message': '',
                'payload': str(body),
                'additional_properties': '',
                'error': ValueError.__name__,
                'error_trace': lambda x: 'Sylvanas error value' in x,
            })

        AssertHandlerLog()

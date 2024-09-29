from sylvanas.Exceptions import ArgumentException
from sylvanas.Handler import Handler
from sylvanas.misc.Assert import Assert
from sylvanas.misc.Guid import Guid
from unittests.config.BaseTest import BaseTest


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
        print('\ncoucou')


class TestHandler(BaseTest):

    def test_Handler(self):
        Assert.hasRaise(TypeError, CustomCommandHandler, None, {}, msg='DbSession must be type of Session')
        Assert.hasRaise(TypeError, CustomCommandHandler, self.dbSession, None, msg='Body format is not valid, dict expected')
        Assert.hasRaise(ArgumentException, CustomCommandHandler, self.dbSession, {}, msg="'user_id' is a required property")

    def test_Schema(self):
        userId = Guid.new()
        h = CustomCommandHandler(self.dbSession, {'user_id': userId})

        Assert.areEqual(h.getAttribute('user_id'), userId)

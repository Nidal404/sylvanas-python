from sylvanas.Exceptions import DevException
from sylvanas.database.Entities import Setting
from sylvanas.handlers.DeleteEntityCommandHandler import DeleteEntityCommandHandler
from sylvanas.misc.Assert import Assert
from sylvanas.misc.Guid import Guid
from unittests.config.BaseTest import HandlerBaseTest
from unittests.config.TestEntities import _Xyqenr2DeletableTestClass


class _Xyqenr1TestClass:
    pass


class TestDeleteEntityCommandHandler(HandlerBaseTest):
    HANDLER = DeleteEntityCommandHandler

    def test_WrongArgs(self):
        Assert.hasRaise(DevException, self.runHandler, {'id': Guid.new()}, msg='Model class must be provided in kwargs')
        Assert.hasRaise(DevException, self.runHandler, {'id': Guid.new()}, model_class=_Xyqenr1TestClass, msg='Model class must be a subclass of Entity')
        Assert.hasRaise(DevException, self.runHandler, {'id': Guid.new()}, model_class=Setting, msg='Model class must be a subclass of DeletableEntity')

    def test_Handler(self):
        # PREPARE
        instance = _Xyqenr2DeletableTestClass()
        instance.id = Guid.new()
        self.dbSession.add(instance)
        self.dbSession.commit()

        # TEST
        self.runHandler({'id': instance.id}, model_class=_Xyqenr2DeletableTestClass)
        self.refreshSession()

        result = self.dbSession.query(_Xyqenr2DeletableTestClass).one()
        Assert.isTrue(result.is_deleted)
        Assert.isTimestamp(result.deleted_datetime)

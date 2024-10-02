from sylvanas.Exceptions import ApplicationException, DevException
from sylvanas.Handler import Handler
from sylvanas.database.Entity import DeletableEntity, Entity
from sylvanas.utils.DateUtils import DateUtils


class DeleteEntityCommandHandler(Handler):

    def defineSchema(self):
        return {
            "type": "object",
            "trim": ["id"],
            "required": ["id"],
            "properties": {
                "id": {"type": "string", "minLength": 36, "maxLength": 36},
            }
        }

    def handle(self, **kwargs):
        model_class = kwargs.get('model_class')

        if model_class is None:
            raise DevException("Model class must be provided in kwargs")
        if not issubclass(model_class, Entity):
            raise DevException("Model class must be a subclass of Entity")
        if not issubclass(model_class, DeletableEntity):
            raise DevException("Model class must be a subclass of DeletableEntity")

        entity: Entity = self.dbSession \
            .query(model_class) \
            .where(model_class.id == self.getAttribute('id')) \
            .one_or_none()

        if entity is None:
            raise ApplicationException(f'{model_class} with id {self.getAttribute('id')} not found')
        if entity.is_deleted:
            return

        entity.is_deleted = True
        entity.deleted_datetime = DateUtils.UtcNow()

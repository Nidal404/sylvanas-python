from abc import ABC, abstractmethod

from sqlalchemy import Integer, String, Boolean
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped

from sylvanas.Utils.DateUtils import DateUtils


class Entity(DeclarativeBase):
    MYSQL_ENGINE = 'InnoDB'
    MYSQL_COLLATE = 'utf8mb4_unicode_ci'

    __table_args__ = {
        'mysql_engine': MYSQL_ENGINE,
        'mysql_collate': MYSQL_COLLATE
    }

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    created_datetime: Mapped[int] = mapped_column(Integer(), nullable=False, default=DateUtils.UtcNow())


class DeletableEntity:
    is_deleted: Mapped[bool] = mapped_column(Boolean(), nullable=False, default=False)
    deleted_datetime: Mapped[int] = mapped_column(Integer(), nullable=True)


class EntityFactory(ABC):

    @staticmethod
    @abstractmethod
    def create(**kwargs) -> Entity:
        raise NotImplementedError()

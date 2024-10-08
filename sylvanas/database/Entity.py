from sqlalchemy import Integer, String, Boolean, CHAR
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped

from sylvanas.utils.DateUtils import DateUtils


class Entity(DeclarativeBase):
    MYSQL_ENGINE = 'InnoDB'
    MYSQL_COLLATE = 'utf8mb4_unicode_ci'

    __table_args__ = {
        'mysql_engine': MYSQL_ENGINE,
        'mysql_collate': MYSQL_COLLATE
    }

    id: Mapped[str] = mapped_column(CHAR(36), primary_key=True)
    created_datetime: Mapped[int] = mapped_column(Integer(), nullable=False, default=DateUtils.UtcNow())


class DeletableEntity:
    is_deleted: Mapped[bool] = mapped_column(Boolean(), nullable=False, default=False)
    deleted_datetime: Mapped[int] = mapped_column(Integer(), nullable=True)

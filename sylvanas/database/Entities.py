from sqlalchemy import Text, String, SmallInteger
from sqlalchemy.orm import Mapped, mapped_column

from sylvanas.database.Entity import Entity


class Setting(Entity):
    __tablename__ = "settings"

    description: Mapped[str] = mapped_column(String(150), nullable=False)
    value: Mapped[str] = mapped_column(String(255), nullable=False)


class HandlerLog(Entity):
    __tablename__ = 'handlers_logs'

    handler_name: Mapped[str] = mapped_column(String(150), nullable=False)
    severity_level: Mapped[int] = mapped_column(SmallInteger(), nullable=False)
    payload: Mapped[str] = mapped_column(Text(), nullable=False)
    additional_properties: Mapped[str] = mapped_column(Text(), nullable=False)
    message: Mapped[str] = mapped_column(String(255), nullable=False)
    error: Mapped[str] = mapped_column(String(150), nullable=False, default='')  # Exception / Error
    error_trace: Mapped[str] = mapped_column(Text(), nullable=False, default='')  # Traceback

import os

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from sylvanas.Enums import ProjectEnvironmentType
from sylvanas.ProjectEnvironment import ProjectEnvironment, ProjectEnvironmentKey
from sylvanas.database.Database import Database
from sylvanas.database.Entity import Entity, DeletableEntity

os.environ[ProjectEnvironmentKey.ENVIRONMENT] = ProjectEnvironmentType.TEST.value
os.environ[ProjectEnvironmentKey.DEBUG] = 'true'
os.environ[ProjectEnvironmentKey.DB_HOST] = 'localhost'
os.environ[ProjectEnvironmentKey.DB_USERNAME] = 'root'
os.environ[ProjectEnvironmentKey.DB_PASSWORD] = ''
os.environ[ProjectEnvironmentKey.DB_NAME] = 'marco'
os.environ[ProjectEnvironmentKey.DB_ECHO] = 'true'

ProjectEnvironment.addToCache()

class Setting(Entity, DeletableEntity):
    __tablename__ = "settings"

    description: Mapped[str] = mapped_column(String(150), nullable=False)
    value: Mapped[str] = mapped_column(String(255), nullable=False)





Database(engine) \
    .create(raiseIfExists=False) \
    .createTables(drop=True)

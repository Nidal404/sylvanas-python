from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy_utils import database_exists

from sylvanas.ProjectEnvironment import ProjectEnvironment as Env, ProjectEnvironment
from sylvanas.database.Database import Database, dbSessionScope
from sylvanas.database.DatabaseCommand import DatabaseCommand
from sylvanas.database.Entity import Entity, DeletableEntity
from sylvanas.misc.Assert import Assert
from sylvanas.misc.Guid import Guid


class Setting(Entity, DeletableEntity):
    __tablename__ = "settings"

    description: Mapped[str] = mapped_column(String(150), nullable=False)
    value: Mapped[str] = mapped_column(String(255), nullable=False)


class TestDatabase:

    def test_DatabaseCreation(self):
        databaseName = 'unittests_db'
        engineUrl = 'mysql+pymysql://{db_username}:{db_password}@{db_host}/{db_name}'
        engineUrl = engineUrl.format(
            db_username=ProjectEnvironment.getDatabaseUsername(),
            db_password=ProjectEnvironment.getDatabasePassword(),
            db_host=ProjectEnvironment.getDatabaseHost(),
            db_name=databaseName,
        )

        print(f'\n{engineUrl}')
        engine = Database.createEngine(engineUrl, echo=Env.isDatabaseQueriesTraceEnable())

        database = Database(engine) \
            .create(raiseIfExists=False) \
            .createTables(drop=True)

        # Base générée
        Assert.isTrue(database_exists(engine.url))

        settingId = Guid.new()

        with (dbSessionScope(database.openDbSession()) as dbSession):
            setting = Setting()
            setting.id = settingId
            setting.description = 'description'
            setting.value = str(1)
            setting.is_deleted = True
            dbSession.add(setting)

        # Nouvelle entrée
        with (dbSessionScope(database.openDbSession()) as dbSession):
            setting: Setting = dbSession.query(Setting).get(settingId)
            Assert.isNotNone(setting)
            Assert.isTrue(setting.is_deleted)

        # On supprime la db
        DatabaseCommand(databaseName, Env.getDatabaseUsername()).dropDb()

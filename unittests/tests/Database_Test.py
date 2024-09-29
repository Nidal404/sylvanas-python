from sqlalchemy_utils import database_exists

from sylvanas.ProjectEnvironment import ProjectEnvironment as Env, ProjectEnvironment
from sylvanas.database.Database import Database, dbSessionScope
from sylvanas.database.DatabaseCommand import DatabaseCommand
from sylvanas.database.Entities import Setting
from sylvanas.misc.Assert import Assert
from sylvanas.misc.Guid import Guid


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

        # On supprime la db
        DatabaseCommand(databaseName, Env.getDatabaseUsername()).dropDb()

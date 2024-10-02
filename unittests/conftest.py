import os
from time import sleep

from sylvanas.Enums import ProjectEnvironmentType
from sylvanas.ProjectEnvironment import ProjectEnvironmentKey, ProjectEnvironment
from sylvanas.database.Database import Database
from sylvanas.database.DatabaseCommand import DatabaseCommand

os.environ[ProjectEnvironmentKey.ENVIRONMENT] = ProjectEnvironmentType.TEST.value
os.environ[ProjectEnvironmentKey.DEBUG] = 'false'
os.environ[ProjectEnvironmentKey.DB_HOST] = 'localhost'
os.environ[ProjectEnvironmentKey.DB_USERNAME] = 'root'
os.environ[ProjectEnvironmentKey.DB_PASSWORD] = ''
os.environ[ProjectEnvironmentKey.DB_NAME] = 'unittests'
os.environ[ProjectEnvironmentKey.DB_ECHO] = 'false'


def pytest_sessionstart(session):  # before session.main() is called
    ProjectEnvironment.loadAndCacheEnvironmentVariables()
    engine = Database.createEngine(ProjectEnvironment.getDatabaseUrl(), echo=ProjectEnvironment.isDatabaseQueriesTraceEnable())

    recreateDb = True

    # Create de la base de données
    if recreateDb:
        import sylvanas.database.Entities
        import unittests.config.TestEntities
        DatabaseCommand(ProjectEnvironment.getDatabaseName(), ProjectEnvironment.getDatabaseUsername()).dropDb()
        sleep(2)

        Database(engine).create(raiseIfExists=False).createTables(drop=True)

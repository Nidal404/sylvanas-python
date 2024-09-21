import os

from sylvanas.Enums import ProjectEnvironmentType
from sylvanas.ProjectEnvironment import ProjectEnvironmentKey, ProjectEnvironment

os.environ[ProjectEnvironmentKey.ENVIRONMENT] = ProjectEnvironmentType.TEST.value
os.environ[ProjectEnvironmentKey.DEBUG] = 'false'
os.environ[ProjectEnvironmentKey.DB_HOST] = 'localhost'
os.environ[ProjectEnvironmentKey.DB_USERNAME] = 'root'
os.environ[ProjectEnvironmentKey.DB_PASSWORD] = ''
os.environ[ProjectEnvironmentKey.DB_NAME] = 'unittests'
os.environ[ProjectEnvironmentKey.DB_ECHO] = 'false'


def pytest_sessionstart(session):  # before session.main() is called
    ProjectEnvironment.loadAndCacheEnvironmentVariables()

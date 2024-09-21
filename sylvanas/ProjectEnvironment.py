import os
from abc import ABC
from typing import Dict, Type

from sylvanas.Enums import ProjectEnvironmentType
from sylvanas.Exceptions import ArgumentException
from sylvanas.Utils.TextFormatUtils import TextFormatUtils

ENVIRONMENT_CACHE: Dict[str, str] = {}


class ProjectEnvironmentKey(ABC):
    ENVIRONMENT = 'ENVIRONMENT'
    DEBUG = 'DEBUG'
    DB_HOST = 'DB_HOST'
    DB_USERNAME = 'DB_USERNAME'
    DB_PASSWORD = 'DB_PASSWORD'
    DB_NAME = 'DB_NAME'
    DB_ECHO = 'DB_ECHO'


class ProjectEnvironment:

    @staticmethod
    def loadAndCacheEnvironmentVariables():
        global ENVIRONMENT_CACHE

        ProjectEnvironment.isEnvVarExists(ProjectEnvironmentKey.ENVIRONMENT)
        ProjectEnvironment.isEnvVarExists(ProjectEnvironmentKey.DEBUG)
        ProjectEnvironment.isEnvVarExists(ProjectEnvironmentKey.DB_HOST)
        ProjectEnvironment.isEnvVarExists(ProjectEnvironmentKey.DB_USERNAME)
        ProjectEnvironment.isEnvVarExists(ProjectEnvironmentKey.DB_PASSWORD)
        ProjectEnvironment.isEnvVarExists(ProjectEnvironmentKey.DB_NAME)
        ProjectEnvironment.isEnvVarExists(ProjectEnvironmentKey.DB_ECHO)

        for key, value in os.environ.items():
            ENVIRONMENT_CACHE[key] = value

    @staticmethod
    def isEnvVarExists(key: str):
        if os.getenv(key) is None:
            raise Exception(f'Missing {key} environment variable')

    @staticmethod
    def getEnvVar(expectedType: Type, key: str):
        if key not in ENVIRONMENT_CACHE:
            raise ArgumentException(f'{key} environment key not found')

        value = ENVIRONMENT_CACHE[key]

        if expectedType == bool:
            return TextFormatUtils.strToBool(value)
        if expectedType == str:
            return value

        raise ValueError(f'{key} environment key not found')

    ######################
    # ENVIRONMENT
    ######################

    @staticmethod
    def debug() -> bool:
        return ProjectEnvironment.getEnvVar(bool, ProjectEnvironmentKey.DEBUG)

    @staticmethod
    def inDevMode() -> bool:
        return ProjectEnvironment \
            .getEnvVar(str, ProjectEnvironmentKey.ENVIRONMENT) == ProjectEnvironmentType.DEVELOPMENT.value

    @staticmethod
    def inProductionMode() -> bool:
        return ProjectEnvironment \
            .getEnvVar(str, ProjectEnvironmentKey.ENVIRONMENT) == ProjectEnvironmentType.PRODUCTION.value

    @staticmethod
    def inTestMode() -> bool:
        return ProjectEnvironment \
            .getEnvVar(str, ProjectEnvironmentKey.ENVIRONMENT) == ProjectEnvironmentType.TEST.value

    ######################
    # DATABASE
    ######################

    @staticmethod
    def traceDatabaseQueries() -> bool:
        return ProjectEnvironment.getEnvVar(bool, ProjectEnvironmentKey.DB_ECHO)

    @staticmethod
    def getDatabaseUsername():
        return ProjectEnvironment.getEnvVar(str, ProjectEnvironmentKey.DB_USERNAME)

    @staticmethod
    def getDatabaseName():
        return ProjectEnvironment.getEnvVar(str, ProjectEnvironmentKey.DB_NAME)

    @staticmethod
    def getDatabasePassword():
        return ProjectEnvironment.getEnvVar(str, ProjectEnvironmentKey.DB_PASSWORD)

    @staticmethod
    def getDatabaseHost():
        return ProjectEnvironment.getEnvVar(str, ProjectEnvironmentKey.DB_HOST)

    @staticmethod
    def getDatabaseUrl() -> str:
        url = 'mysql+pymysql://{db_username}:{db_password}@{db_host}/{db_name}'
        return url.format(
            db_username=ProjectEnvironment.getDatabaseUsername(),
            db_password=ProjectEnvironment.getDatabasePassword(),
            db_host=ProjectEnvironment.getDatabaseHost(),
            db_name=ProjectEnvironment.getDatabaseName(),
        )

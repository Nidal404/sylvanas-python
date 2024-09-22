from abc import ABC

from sylvanas.ProjectEnvironment import ProjectEnvironment
from sylvanas.database.Database import Database


class BaseTest(ABC):

    @property
    def dbSession(self):
        engine = Database.createEngine(ProjectEnvironment.getDatabaseUrl())
        return Database(engine).openDbSession()

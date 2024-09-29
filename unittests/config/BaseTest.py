from abc import ABC
from typing import Optional, Dict

from sqlalchemy.orm import Session

from sylvanas.Handler import Handler
from sylvanas.ProjectEnvironment import ProjectEnvironment
from sylvanas.database.Database import Database, dbSessionScope
from sylvanas.database.Entity import Entity


class BaseTest(ABC):
    _dbSession: Optional[Session] = None
    _engine = Database.createEngine(ProjectEnvironment.getDatabaseUrl())

    @property
    def dbSession(self) -> Session:
        if self._dbSession is None:
            self._dbSession = Database(self._engine).openDbSession()  # Create the session
        return self._dbSession

    def setup_method(self):
        self.clear_database()  # Clear the database before each test

    def clear_database(self):
        Entity.metadata.reflect(bind=self._engine)

        with (dbSessionScope(Database(self._engine).openDbSession()) as dbSession):
            for table in reversed(Entity.metadata.sorted_tables):
                dbSession.execute(table.delete())

    def teardown(self):
        """Teardown method to close the session after tests."""
        if self._dbSession is not None:
            self._dbSession.close()
            self._dbSession = None


class HandlerBaseTest(BaseTest, ABC):
    HANDLER = None

    def runHandler(self, body: Dict) -> Handler:
        if self.HANDLER is None:
            raise ValueError('You must set the HANDLER variable.')

        with (dbSessionScope(Database(self._engine).openDbSession()) as dbSession):
            handler = self.HANDLER(dbSession, body)
            handler.handle()
            return handler

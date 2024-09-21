from contextlib import contextmanager

from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy_utils import create_database, database_exists

from sylvanas.Enums import ExceptionLevel
from sylvanas.Exceptions import ApplicationException
from sylvanas.database.Entity import Entity


class Database:

    @staticmethod
    def createEngine(url: str, **kwargs) -> Engine:
        return create_engine(url, **kwargs)

    def __init__(self, engine: Engine):
        self.engine = engine

    def create(self, raiseIfExists: bool = True):
        databaseExists = database_exists(self.engine.url)

        if databaseExists and raiseIfExists:
            raise ApplicationException(f"Database '{self.engine.url}' already exists", ExceptionLevel.ERROR)
        elif not databaseExists:
            create_database(self.engine.url)
            print(f"Database '{self.engine.url} has been created")
        return self

    def dropTables(self):
        Entity.metadata.drop_all(self.engine)
        return self

    def createTables(self, drop: bool = False):
        if drop:
            self.dropTables()

        Entity.metadata.create_all(self.engine)
        return self

    def openDbSession(self) -> Session:
        session = sessionmaker(bind=self.engine)
        return session()


@contextmanager
def dbSessionScope(session):
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()

from contextlib import contextmanager
from sqlmodel import Session, create_engine, SQLModel

DB_URL = 'sqlite:///records.sqlite'
engine = create_engine(DB_URL, echo=True)


@contextmanager
def get_session():
    session = Session(engine)
    try:
        yield session
    finally:
        session.close()


def init():
    SQLModel.metadata.create_all(engine)
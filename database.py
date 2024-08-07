from sqlmodel import Session, create_engine, SQLModel

DB_URL = 'sqlite:///records.sqlite'
engine = create_engine(DB_URL)


def get_session():
    with Session(engine) as session:
        yield session


def init():
    SQLModel.metadata.create_all(engine)

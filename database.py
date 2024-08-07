from sqlmodel import Session, create_engine, SQLModel

DB_URL = 'sqlite:///records.sqlite'
engine = create_engine(DB_URL, echo=True)


def get_session() -> Session:
    with Session(engine) as session:
        yield session


def init():
    SQLModel.metadata.create_all(engine)

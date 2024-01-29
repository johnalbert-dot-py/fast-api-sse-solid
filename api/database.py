from sqlmodel import create_engine, SQLModel, Session, select
from user import model as user_model
from post import model as post_model

DATABASE_URL = "sqlite:///./sse_app.db"
engine = create_engine(
    DATABASE_URL, echo=True, connect_args={"check_same_thread": False}
)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def drop_db_and_tables():
    SQLModel.metadata.drop_all(engine)


if __name__ == "__main__":
    drop_db_and_tables()
    create_db_and_tables()

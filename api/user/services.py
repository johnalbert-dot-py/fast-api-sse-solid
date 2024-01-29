from . import model
from database import engine, Session, select
from fastapi import HTTPException


def get_users():
    with Session(engine) as session:
        user = model.User
        statement = select(user.id, user.username, user.email)
        results = session.exec(statement)
        # results.fetchmany()
        return results.fetchmany()


def get_user_by_id_or_email(user_id: int = None, email: str = None):
    with Session(engine) as session:
        statement = select(model.User).where(
            (model.User.id == user_id) | (model.User.email == email)
        )
        results = session.exec(statement)
        return results.first()


def create_user(user):
    with Session(engine) as session:
        user_found = get_user_by_id_or_email(email=user.email)
        if user_found:
            raise HTTPException(status_code=400, detail="User already exists")

    with Session(engine) as session:
        db_user = model.User(
            username=user.username,
            email=user.email,
            password=user.password,
        )
        session.add(db_user)
        session.commit()
        session.refresh(db_user)
        return db_user

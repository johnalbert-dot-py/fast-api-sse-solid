from . import model
from user.model import User
from database import engine, Session, select
from fastapi.encoders import jsonable_encoder
import json


def get_post_by_id(post_id: int):
    with Session(engine) as session:
        statement = select(model.Post).where(model.Post.id == post_id)
        results = session.exec(statement)
        post = results.one_or_none()
        if post is None:
            return None
        result = post.model_dump()
        return result


def get_all_posts(as_dict=False):
    with Session(engine) as session:
        statement = select(
            model.Post.id,
            model.Post.title,
            model.Post.content,
            model.Post.user_id,
            model.Post.created_at,
            model.Post.updated_at,
            User.username,
            User.email,
        ).join(User, model.Post.user_id == User.id)
        results = session.exec(statement)
        posts = results.all()

        if as_dict:
            return [
                jsonable_encoder(model.Post(**post._mapping).model_dump())
                for post in posts
            ]
        return posts


def create_post(post):
    with Session(engine) as session:
        db_post = model.Post(
            title=post.title,
            content=post.content,
            user_id=post.user_id,
        )
        session.add(db_post)
        session.commit()
        session.refresh(db_post)
        return db_post


def delete_post_by_id(post_id: int):
    with Session(engine) as session:
        statement = select(model.Post).where(model.Post.id == post_id)
        results = session.exec(statement)
        post = results.one_or_none()
        if post is None:
            return None
        session.delete(post)
        session.commit()
        return post.model_dump()

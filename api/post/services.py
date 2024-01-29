from . import model
from user.model import User
from database import engine, Session, select


def get_post_by_id(post_id: int):
    with Session(engine) as session:
        statement = select(model.Post).where(model.Post.id == post_id)
        results = session.exec(statement)
        post = results.one_or_none()
        if post is None:
            return None
        result = post.model_dump()
        return result


def get_all_posts():
    with Session(engine) as session:
        statement = select(
            model.Post.id,
            model.Post.title,
            model.Post.content,
            model.Post.user_id,
            User.username,
            User.email,
        ).join(User, model.Post.user_id == User.id)
        results = session.exec(statement)
        posts = results.fetchall()
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

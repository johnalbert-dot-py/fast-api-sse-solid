from typing import Optional, List, TYPE_CHECKING
from sqlmodel import Field, Relationship
from database import SQLModel
from datetime import datetime


if TYPE_CHECKING:
    from user.model import User


class Post(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(nullable=False)
    content: str = Field(nullable=False)
    user: "User" = Relationship(back_populates="posts")
    user_id: int = Field(nullable=False, foreign_key="user.id")

    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)


class PostCreate(SQLModel):
    title: str
    content: str
    user_id: int


from user.model import User


class PostView(SQLModel):
    id: int
    title: str
    content: str
    user_id: int
    username: str
    email: str
    created_at: datetime
    updated_at: datetime

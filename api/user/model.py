from typing import Optional, List, TYPE_CHECKING
from sqlmodel import Field, Relationship
from database import SQLModel
from datetime import datetime

# from post.model import Post
if TYPE_CHECKING:
    from post.model import Post


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(default=None, unique=True, index=True)
    email: str = Field(default=None, unique=True, index=True)
    password: str = Field(default=None)
    is_active: bool = Field(default=True)

    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)

    posts: List["Post"] = Relationship(back_populates="user")

    # updated_at: DateTime = Field(default=None)
    # created_at: DateTime = Field(default=None)


class UserCreate(SQLModel):
    username: str
    email: str
    password: str

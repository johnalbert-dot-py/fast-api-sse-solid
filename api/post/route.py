from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from typing import List
from .services import create_post, get_all_posts, get_post_by_id
from .model import PostCreate, Post, PostView

router = APIRouter(
    prefix="/post",
    tags=["user"],
    responses={404: {"description": "Not found"}},
)


@router.post("/", response_model=Post)
def create_new_post(post: PostCreate):
    created = create_post(post=post)
    return created.model_dump()


@router.get("/", response_model=List[PostView])
def posts():
    posts = get_all_posts()
    return posts


@router.get(
    "/{post_id}",
    response_model=Post,
)
def get_post(post_id: int):
    post = get_post_by_id(post_id=post_id)
    if post is None:
        raise HTTPException(404, detail="Post not found")
    return post

from fastapi import APIRouter
from typing import List
from .services import create_user, get_users
from .model import UserCreate

router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
def get_list_of_users():
    users = get_users()
    return [dict(data._mapping) for data in users]


@router.post("/")
def create_new_user(user: UserCreate):
    created = create_user(user=user)
    return created.model_dump(include={"id", "username", "email", "created_at"})

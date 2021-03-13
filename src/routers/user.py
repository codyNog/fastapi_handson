from fastapi import APIRouter
from typing import List
from entities.user import User

user_router = APIRouter()


@user_router.post('user')
def create_user(user: User) -> User:
    from main import backend
    return backend.user_repos.create_user(user)


@user_router.get('/user/{id}')
def get_user(id: str) -> User:
    from main import backend
    return backend.user_repos.get_user(id)


@user_router.patch('/user/{id}')
def update_user(user: User) -> User:
    from main import backend
    return backend.user_repos.update_user(user)


@user_router.get('/users')
def get_users() -> List[User]:
    from main import backend
    return backend.user_repos.get_users()

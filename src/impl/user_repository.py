from typing import List
from use_cases.user_repository import UserRepository
from entities.user import User


class UserRepositoryImpl(UserRepository):
    def get_user(self, id: str) -> User:
        return {'id': id, 'name': 'foo'}

    def get_users(self) -> List[User]:
        return []

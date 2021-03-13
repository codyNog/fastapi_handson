import uuid
from typing import List
from use_cases.user_repository import UserRepository
from entities.user import User


class UserRepositoryImpl(UserRepository):
    def create_user(self, user: User) -> User:
        user: User = {'id': str(uuid.uuid4()), 'profile': user.profile, 'properties': user.properties}
        return user

    def get_user(self, id: str) -> User:
        user: User = {'id': id, 'profile': {'first_name': 'jeff', 'family_name': 'kendrick', 'age': 28}, 'properties': []}
        return user

    def update_user(self, user: User) -> User:
        return user

    def get_users(self) -> List[User]:
        users = []
        return users

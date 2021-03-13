from abc import ABCMeta, abstractmethod
from typing import Iterator, List
from entities.user import User

Created = bool


class UserRepository(metaclass=ABCMeta):
    @abstractmethod
    def create_user(self, user: User) -> Iterator[User]:
        raise NotImplementedError

    @abstractmethod
    def get_user(self, id: str) -> Iterator[User]:
        raise NotImplementedError

    @abstractmethod
    def update_user(self, user: User) -> Iterator[User]:
        raise NotImplementedError

    @abstractmethod
    def get_users(self) -> Iterator[List[User]]:
        raise NotImplementedError

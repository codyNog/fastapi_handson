from abc import ABCMeta, abstractmethod
from typing import Iterator, List
from entities.property import Property

Created = bool


class PropertyRepository(metaclass=ABCMeta):
    @abstractmethod
    def create_property(self, property: Property) -> Iterator[Property]:
        raise NotImplementedError

    @abstractmethod
    def get_property(self, id: str) -> Iterator[Property]:
        raise NotImplementedError

    @abstractmethod
    def update_property(self, property: Property) -> Iterator[Property]:
        raise NotImplementedError

    @abstractmethod
    def get_properties(self) -> Iterator[List[Property]]:
        raise NotImplementedError

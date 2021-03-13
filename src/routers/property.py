from fastapi import APIRouter
from typing import List
from entities.property import Property

property_router = APIRouter()


@property_router.post('/property')
def create_property(property: Property) -> Property:
    from main import backend
    return backend.property_repos.create_property(property)


@property_router.get('/property/{id}')
def get_property(id: str) -> Property:
    from main import backend
    return backend.property_repos.get_property(id)


@property_router.patch('/property/{id}')
def update_property(property: Property) -> Property:
    from main import backend
    return backend.property_repos.update_property(property)


@property_router.get('/properties')
def get_properties() -> List[Property]:
    from main import backend
    return backend.property_repos.get_properties()

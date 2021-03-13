from pydantic import BaseModel
from typing import List
from entities.property import Property


class Profile(BaseModel):
    first_name: str
    family_name: str
    age: int


class User(BaseModel):
    id: str
    profile: Profile
    properties: List[Property]

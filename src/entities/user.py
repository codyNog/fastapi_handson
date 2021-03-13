from pydantic import BaseModel
from typing import List


class Profile(BaseModel):
    first_name: str
    family_name: str
    age: int


class Address(BaseModel):
    prefecture: str
    city: str
    other_address: str


class Property(BaseModel):
    id: str
    value: int
    address: Address


class User(BaseModel):
    id: str
    profile: Profile
    properties: List[Property]

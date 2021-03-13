from pydantic import BaseModel


class Address(BaseModel):
    prefecture: str
    city: str
    other_address: str


class Property(BaseModel):
    id: str
    value: int
    address: Address

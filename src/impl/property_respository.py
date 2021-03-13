import uuid
from typing import List
from use_cases.property_repository import PropertyRepository
from entities.property import Property


class PropertyRepositoryImpl(PropertyRepository):
    def create_property(self, property: Property) -> Property:
        property.id = uuid.uuid4()
        return property

    def get_property(self, id: str) -> Property:
        return {}

    def update_property(self, id: str) -> Property:
        return {}

    def get_properties(self) -> List[Property]:
        return []

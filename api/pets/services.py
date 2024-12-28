import dataclasses
from user import services as user_service

from typing import TYPE_CHECKING
from django.conf import settings
from . import models as pet_models

if TYPE_CHECKING:
    from .models import Pets


@dataclasses.dataclass
class PetDataClass:
    name: str
    species: str
    breed: str
    age: int
    weight: float
    medical_condition: str
    user: user_service.UserDataClass = None
    id: int = None

    @classmethod
    def from_instance(cls, pet_model: "Pets") -> "PetDataClass":
        return cls(
            name=pet_model.name,
            species=pet_model.species,
            breed=pet_model.breed,
            age=pet_model.age,
            weight=pet_model.weight,
            medical_condition=pet_model.medical_condition,
            id=pet_model.id,
            user=pet_model.user,
        )


def create_pet(user, pet_dc: "PetDataClass") -> "PetDataClass":
    pet_create = pet_models.Pets.objects.create(
        name=pet_dc.name,
        species=pet_dc.species,
        breed=pet_dc.breed,
        age=pet_dc.age,
        weight=pet_dc.weight,
        medical_condition=pet_dc.medical_condition,
        user=user,
    )

    return PetDataClass.from_instance(pet_model=pet_create)

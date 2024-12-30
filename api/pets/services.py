import dataclasses
from rest_framework import exceptions
from user import services as user_service

from django.shortcuts import get_object_or_404

from typing import TYPE_CHECKING
from . import models as pet_models

if TYPE_CHECKING:
    from .models import Pets
    from user.models import User


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


def get_user_pet(user: "User") -> list["PetDataClass"]:
    user_pets = pet_models.Pets.objects.filter(user=user)

    return [PetDataClass.from_instance(single_pet) for single_pet in user_pets]


def get_user_pet_detail(pet_id: int) -> "PetDataClass":
    pet = get_object_or_404(pet_models.Pets, pk=pet_id)

    return PetDataClass.from_instance(pet_model=pet)


def delete_user_pet(user: "User", pet_id: int) -> "PetDataClass":
    pet = get_object_or_404(pet_models.Pets, pk=pet_id)

    if user.id != pet.user.id:
        raise exceptions.PermissionDenied("You're not the user fool!")
    pet.delete()


def update_user_pet(user: "User", pet_id: int, pet_data: "PetDataClass"):
    pet = get_object_or_404(pet_models.Pets, pk=pet_id)

    if user.id != pet.user.id:
        raise exceptions.PermissionDenied("You're not the user fool!")

    pet.name = pet_data.name
    pet.species = pet_data.species
    pet.breed = pet_data.breed
    pet.age = pet_data.age
    pet.weight = pet_data.weight
    pet.medical_condition = pet_data.medical_condition
    pet.save()

    return PetDataClass.from_instance(pet_model=pet)

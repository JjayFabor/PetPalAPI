import dataclasses
from typing import TYPE_CHECKING

from . import models

if TYPE_CHECKING:
    from .models import User


@dataclasses.dataclass
class UserDataClass:
    first_name: str
    last_name: str
    email: str
    location: str
    is_service_provider: bool
    phone_number: int
    password: str = None
    id: int = None

    @classmethod
    def from_instance(cls, user: "User") -> "UserDataClass":
        return cls(
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            id=user.id,
            location=user.location,
            is_service_provider=user.is_service_provider,
            phone_number=user.phone_number,
        )


def create_user(user_dc: "UserDataClass") -> "UserDataClass":
    instance = models.User(
        first_name=user_dc.first_name,
        last_name=user_dc.last_name,
        email=user_dc.email,
        location=user_dc.location,
        is_service_provider=user_dc.is_service_provider,
        phone_number=user_dc.phone_number,
    )

    if user_dc.password is not None:
        instance.set_password(user_dc.password)

    instance.save()

    return UserDataClass.from_instance(instance)

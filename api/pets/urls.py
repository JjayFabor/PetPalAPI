from django.urls import path
from . import views

urlpatterns = [
    path("pets/", views.PetCreateListApi.as_view(), name="pets"),
    path(
        "pets/<int:pet_id>/",
        views.PetRetrieveUpdateDeleteApi.as_view(),
        name="pet_detail",
    ),
]

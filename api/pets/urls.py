from django.urls import path
from . import views

urlpatterns = [
    path("pets/", views.PetCreateListApi.as_view(), name="pets"),
]

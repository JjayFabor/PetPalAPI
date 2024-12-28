from django.contrib import admin
from . import models


class _PetsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "species",
        "breed",
        "age",
        "weight",
        "medical_condition",
    )


admin.site.register(models.Pets, _PetsAdmin)

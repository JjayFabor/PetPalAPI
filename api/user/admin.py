from django.contrib import admin
from . import models


class _UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "email",
        "phone_number",
    )


admin.site.register(models.User, _UserAdmin)

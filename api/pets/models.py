from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings


class Pets(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="user",
    )

    name = models.CharField(_("Pet Name"), max_length=255)
    species = models.CharField(_("Species"), max_length=255)
    breed = models.CharField(_("Breed"), max_length=255)
    age = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    medical_condition = models.TextField()

# Generated by Django 5.1.4 on 2024-12-28 13:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Pets",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="Pet Name")),
                ("species", models.CharField(max_length=255, verbose_name="Species")),
                ("breed", models.CharField(max_length=255, verbose_name="Breed")),
                ("age", models.IntegerField(default=0)),
                ("weight", models.IntegerField(default=0)),
                ("medical_condition", models.TextField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="user",
                    ),
                ),
            ],
        ),
    ]

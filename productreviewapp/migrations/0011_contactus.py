# Generated by Django 5.1.2 on 2025-01-24 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("productreviewapp", "0010_rename_image_review_rimage_remove_product_review"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contactus",
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
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("message", models.TextField()),
            ],
        ),
    ]

# Generated by Django 5.1.2 on 2025-01-18 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("productreviewapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(upload_to="images"),
        ),
    ]

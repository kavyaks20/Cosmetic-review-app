# Generated by Django 5.1.2 on 2025-01-25 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("productreviewapp", "0011_contactus"),
    ]

    operations = [
        migrations.AddField(
            model_name="review",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]

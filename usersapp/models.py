from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_staff_user = models.BooleanField(default=False)
    is_end_user = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
      # Default for end users
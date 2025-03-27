# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    is_active = models.BooleanField(
        default=False,
        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts."
    )

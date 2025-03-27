from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        if not username:
            raise ValueError("The Username field must be set")
        email = self.normalize_email(email)
        extra_fields.setdefault('is_active', False)  # Set default for regular users
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_active', True)  # Force superuser to be active
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        
        return self.create_user(username, email, password, **extra_fields)


class CustomUser(AbstractUser):
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    is_active = models.BooleanField(
        default=False,
        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts."
    )

    objects = CustomUserManager()  # Use the custom manager

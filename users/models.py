from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name='authenticationapp_user_groups',  # Unique related name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='authenticationapp_user_permissions',  # Unique related name
        blank=True
    )

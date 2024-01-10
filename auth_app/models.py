from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

import uuid

class Employee(AbstractBaseUser, PermissionsMixin):
    key = models.CharField(max_length=100, unique=True, null=False, default=uuid.uuid4)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    password = models.CharField(max_length=100)

    active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    # Agrega los campos que deseas como requeridos para el registro en REQUIRED_FIELDS
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email



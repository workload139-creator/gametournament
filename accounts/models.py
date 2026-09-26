from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):

    ff_uid = models.CharField(max_length=20, unique=True)
    phone = models.CharField(max_length=15)

    wallet = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.username

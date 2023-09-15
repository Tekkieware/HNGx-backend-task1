from typing import Any
from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(null=False, blank=False, max_length=250)
    email = models.CharField(null=True, blank=True, max_length=250)
    country = models.CharField(null=True, blank=True, max_length=250)

    def __str__(self) -> str:
        return self.name


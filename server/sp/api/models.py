# models.py
from django.db import models

# Create your models here.

class Citizen(models.Model):
    alias = models.CharField(max_length=60)

    def __str__(self):
        return self.alias
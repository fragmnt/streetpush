# models.py
from django.db import models

# Create your models here.

class Citizen(models.Model):
    alias = models.CharField(max_length=60)
    created_At = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s, %s' % (self.alias, self.created_At)
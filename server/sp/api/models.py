# models.py
from django.db import models

# Create your models here.

class Citizen(models.Model):
    alias = models.CharField(max_length=60)
    created_At = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s, %s' % (self.alias, self.created_At)

class Alert(models.Model):

    class Severity(models.IntegerChoices):
        SONE = 1
        STWO = 2
        STHREE = 3

    name = models.CharField(max_length=75)
    date_created = models.DateTimeField(auto_now=True)
    description = models.TextField()
    range = models.IntegerField(choices=Severity.choices)

    def __str__(self):
        return '%s, %s _ %s' % (self.name, self.description, self.date_created)

    def is_high_severity(self):
        return self.range in {
            self.range.STHREE,
        }
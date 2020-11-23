# models.py
from django.db import models

# Create your models here.

class Citizen(models.Model):
    alias = models.CharField(max_length=60)
    created_At = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s, %s' % (self.alias, self.created_At)

class Alert(models.Model):

    class SvRange(models.IntegerChoices):
        LOW = 1
        MEDIUM = 2
        HIGH = 3

    name = models.CharField(max_length=75)
    date_created = models.DateTimeField(auto_now=True)
    description = models.TextField()
    severity = models.IntegerField(choices=SvRange.choices, default=1)

    def __str__(self):
        return '%s, %s _ %s' % (self.name, self.description, self.date_created)

    def is_high_severity(self):
        return self.severity in {
            self.range.HIGH,
        }
# models.py
from django.db import models

# Create your models here.

class Citizen(models.Model):
    citizen_id = models.AutoField(primary_key=True, default=0)
    alias = models.CharField(max_length=60)
    created_At = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s, %s' % (self.alias, self.created_At)

class Alert(models.Model):
    class SvRange(models.IntegerChoices):
        LOW = 1
        MEDIUM = 2
        HIGH = 3
    alert_id = models.AutoField(primary_key=True, default=0)
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

class Notification(models.Model):
    notif_id = models.AutoField(primary_key=True, default=0)
    title = models.CharField(max_length=100)
    brief_description = models.TextField()
    date_reported = models.DateTimeField(auto_now=True)
    long = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    lat = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    linked_article_url = models.TextField()

    def __str__(self):
        return 'Notification ID %s : (%s, %s) (%s) (%s, %s) (%s)' % (self.notif_id, self.title, self.brief_description, self.date_reported,
        self.long, self.lat, self.linked_article_url)
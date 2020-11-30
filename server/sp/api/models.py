# models.py
from django.db import models

## For Mandates and GeoPlaces marked on the Map
# For basic information provided by the API

class Alert(models.Model):
    class SvRange(models.IntegerChoices):
        LOW = 1
        MEDIUM = 2
        HIGH = 3
    alert_id = models.AutoField(primary_key=True, blank=True)
    title = models.CharField(max_length=100, default='')
    date_created = models.DateTimeField(auto_now=True)
    description = models.TextField(default='')
    severity = models.IntegerField(choices=SvRange.choices, default=1)
    long = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    lat = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)

    def __str__(self):
        return '%s, %s _ %s' % (self.name, self.description, self.date_created)

    def is_high_severity(self):
        return self.severity in {
            self.range.HIGH,
        }

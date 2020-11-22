# serializers.py
from rest_framework import serializers

from .models import Citizen, Alert

class CitizenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Citizen
        fields = ('alias','created_At')

class AlertSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Alert
        fields = ('name','date_created', 'description', 'range')
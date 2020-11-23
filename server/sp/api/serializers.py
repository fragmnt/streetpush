# serializers.py
from rest_framework import serializers

from .models import Citizen, Alert, Notification

class CitizenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Citizen
        fields = ('alias','created_At')

class AlertSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Alert
        fields = ('name','date_created', 'description', 'severity')

class NotificationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Notification 
        fields = ('title', 'brief_description', 'date_reported', 'long', 'lat', 'linked_article_url')
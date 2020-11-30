# serializers.py
from rest_framework import serializers

from .models import Alert

class AlertSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Alert
        fields = ('title','date_created', 'description', 'severity',  'long', 'lat')


#class MessageSerializer(serializers.HyperlinkedModelSerializer):
#    body = serializers.CharField(required=True)
##   sender = serializers.ReadOnlyField()

#   class Meta:
#      model = Message 
#     fields = ('id', 'body', 'sent_at', 'sender')
# serializers.py
from rest_framework import serializers

from .models import Citizen

class CitizenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Citizen
        fields = ('alias',)
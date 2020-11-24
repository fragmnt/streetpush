from rest_framework import viewsets
from .serializers import CitizenSerializer, AlertSerializer, NotificationSerializer
from .models import Citizen, Alert, Notification

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

import requests
req = requests

class ListCitizens(APIView):
    """
        View to list all citizens in the system.
    """
    def get(self, request):
        """
            Return a list of citizens
        """
        citizens = Citizen.objects.all()
        citizen_serializer = CitizenSerializer(citizens, many=True)
        return Response(citizen_serializer.data)

class CreateCitizen(APIView):
    def post(self, request):
        """
            Create a new citizen
        """
        c = request.data
        citizens = CitizenSerializer(data = c)
        if citizens.is_valid():
            citizens.save()
            return Response(citizens.data, status=201)
        return Response(citizens.errors, status=400)
          
        







## OLD: Create your views here.

class CitizenViewSet(viewsets.ModelViewSet):
    queryset = Citizen.objects.all().order_by('alias')
    serializer_class = CitizenSerializer

class AlertViewSet(viewsets.ModelViewSet):
    queryset = Alert.objects.all().order_by('date_created')
    serializer_class = AlertSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all().order_by('date_reported')
    serializer_class = NotificationSerializer

## MARK: ... other

covid_api_urls = [
    'https://finnhub.io/api/v1/covid19/us',
    'https://corona.lmao.ninja/v2/countries/America?yesterday&strict&query%20',
    
]

@api_view(['GET'])
def covidApiHome(request):
    res = req.get()
    data = res.json()
    return Response({"status": res.status_code, "data": data}, res.status_code)
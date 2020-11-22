from rest_framework import viewsets
from .serializers import CitizenSerializer
from .models import Citizen

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

import requests
req = requests

# Create your views here.

class CitizenViewSet(viewsets.ModelViewSet):
    queryset = Citizen.objects.all().order_by('alias')
    serializer_class = CitizenSerializer

# ... other

@api_view(['GET'])
def covidApiHome(request):
    res = req.get('https://corona.lmao.ninja/v2/continents/Americas?yesterday&strict')
    # data = res.json()
    return Response({"status": res.status_code, "data": res.json()}, res.status_code)
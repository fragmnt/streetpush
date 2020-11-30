from rest_framework import viewsets
from .serializers import AlertSerializer
from .models import  Alert
from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

import requests
req = requests

## MARK: COVID19 API URLS

covid_api_urls = [
    'https://finnhub.io/api/v1/covid19/us',
    'https://corona.lmao.ninja/v2/states/New York?yesterday=',
    'https://api.covidtracking.com/v1/states/ny/info.json',
    'https://api.covidtracking.com/v1/states/ny/daily.json',
]

# Get Stats on New Cases, Deaths in USA. Updated every 10 min.
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def covidApiHome(request):
    res = req.get(covid_api_urls[1])
    data = res.json()
    return Response({"status": res.status_code, "data": data}, res.status_code)

@permission_classes([IsAuthenticated])
@api_view(['GET'])
def covidResources(request):
    res = req.get(covid_api_urls[2])
    data = res.json()
    return Response({ 'status': res.status_code, "data": data }, res.status_code)

@permission_classes([IsAuthenticated])
@api_view(['GET'])
def covidTimeseries(request):
    res = req.get(covid_api_urls[3])
    data = res.json()
    return Response({ 'status': res.status_code, "data": data }, res.status_code)

class AlertViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Alert.objects.all().order_by('date_created')
    serializer_class = AlertSerializer


# Message: Create New, List All, Delete One
#@api_view(['GET'])
#def listAllMessages(request):
#    messages = Message.objects.all()
#    msg_serializer = MessageSerializer(messages, many=True)
#    return Response(msg_serializer.data, status=200)

# @api_view(['POST'])
# def createNewMessage(request):
#    m = request.data
#    messages = MessageSerializer(data = m)
#    if messages.is_valid():
#        messages.save()
#        return Response(messages.data, status=201)
#    return Response(messages.errors, status=400)





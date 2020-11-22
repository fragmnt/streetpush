from rest_framework import viewsets
from .serializers import CitizenSerializer
from .models import Citizen

# Create your views here.

class CitizenViewSet(viewsets.ModelViewSet):
    queryset = Citizen.objects.all().order_by('alias')
    serializer_class = CitizenSerializer

# ... other
from celery import shared_task
from api.models import Citizen

@shared_task
def count_citizens():
    return Citizen.objects.count()
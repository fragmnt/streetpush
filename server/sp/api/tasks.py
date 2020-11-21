from celery import shared_task
from api.models import Update

@shared_task
def blast(x, y):
    return sum(x, y)
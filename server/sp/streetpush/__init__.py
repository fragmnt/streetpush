
# make sure Celery is always imported
from .celery import app as celery_app

__all__ = ('celery_app',)
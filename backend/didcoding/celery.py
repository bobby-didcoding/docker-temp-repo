import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'didcoding.settings')
app = Celery('didcoding')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.timezone = 'Europe/London'

app.autodiscover_tasks()
from django.shortcuts import render
from django.http import HttpResponse

from .tasks import sleepy, add, send_email_task
# Create your views here.

def index(request):
    add.delay(2, 5)
    # sleepy.delay(10)
    send_email_task.delay()
    return HttpResponse('<h1>EMAIL HAS BEEN SENT WITH CELERY!</h1>')
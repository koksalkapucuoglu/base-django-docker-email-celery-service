from __future__ import absolute_import, unicode_literals

from celery import shared_task
from time import sleep
from django.core.mail import send_mail
@shared_task
def add(x,y):
    return x + y

@shared_task
def sleepy(duration):
    sleep(duration)
    return None

@shared_task
def send_email_task():
    sleep(2)
    send_mail(
        'Celery Task Worked!',
        'This is proof the task worked!',
        'koksalkapucuoglu@hotmail.com',
        ['kuspukarze@vusra.com']
    )

    return None

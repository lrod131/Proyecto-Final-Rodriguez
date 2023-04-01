from django.db import models
from django.conf import settings
from datetime import datetime


class Message(models.Model):
    title = models.CharField(max_length=40, default="Mensaje")
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="sender", on_delete=models.CASCADE)
    reciever = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="reciever", on_delete=models.CASCADE)
    content = models.CharField(max_length=300)
    date = models.DateField(default=datetime.now)
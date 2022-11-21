from email import message
from email.policy import default
from pickle import TRUE
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class CustomUser(AbstractUser):
    image = models.ImageField(null=False, blank=True, upload_to = "media/", default='media/default.png')

class Message(models.Model):
    message = models.CharField(max_length=200, null=False, blank=False)
    userA = models.CharField(max_length=150, null=True, blank=True)
    userB = models.CharField(max_length=150, null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
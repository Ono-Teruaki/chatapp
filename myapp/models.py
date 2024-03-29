from email import message
from email.policy import default
from pickle import TRUE
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

#ユーザーモデル
class CustomUser(AbstractUser):
    image = models.ImageField(null=False, blank=True, upload_to = "media/", default='media/default.png')

#送信されたメッセージモデル
class Message(models.Model):
    message = models.CharField(max_length=200, null=False, blank=False)
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='received_messages')
    created_date = models.DateTimeField(default=timezone.now)

from django.contrib import admin
from .models import CustomUser, Message

#管理サイトに色々追加
admin.site.register(CustomUser)
admin.site.register(Message)

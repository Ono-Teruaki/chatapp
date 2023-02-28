from dataclasses import fields
from email import message
from typing import Text
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Message
from django.contrib.auth.forms import AuthenticationForm


#会員登録フォーム
class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username","password1","password2","email","image")

#ログインフォーム
class LoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']
        
#チャットメッセージフォーム
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['message']

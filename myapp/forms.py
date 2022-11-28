from dataclasses import fields
from email import message
from typing import Text
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Message
from django.contrib.auth.forms import AuthenticationForm


class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username","password1","password2","email","image")

class LoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['message', 'userA', 'userB']

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
        name = forms.CharField(
        max_length=30,
        required=False,
        label='Username'
    )

        email = forms.EmailField(
        max_length=254,
        label='E-mailadress'
    )

class Meta:
    model = User
    fields = ('Username', 'email', 'password1', 'password2', )

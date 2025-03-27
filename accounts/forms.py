# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'middle_name', 'last_name']


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=50)
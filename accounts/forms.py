# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser  # Import your CustomUser model

class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser  # Use CustomUser instead of User
        fields = ('username', 'email', 'password1', 'password2')

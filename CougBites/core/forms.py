from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    username = forms.CharField(max_length=16, min_length=4, help_text="Required. 4 - 16 characters. Letters, digits and @/./+/-/_ only.")

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
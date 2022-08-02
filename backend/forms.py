from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=10)
    email = forms.CharField(max_length=10)
    phone = forms.CharField(max_length=10)
    password = forms.CharField(max_length=10)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'phone', 'password')
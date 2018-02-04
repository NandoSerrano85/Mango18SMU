from django import forms
from django.contrib.auth.forms import AuthenticationForm 
from app.models import *            

class LoginForm(forms.Form):
    username = forms.CharField(label='username', max_length=50, required=True)
    password = forms.CharField(label='password', max_length=50, required=True)   

    def save(self):           
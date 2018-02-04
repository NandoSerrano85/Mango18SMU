from django import forms
from django.contrib.auth.forms import AuthenticationForm
from app.models import *    

class LoginForm(forms.Form):
    username = forms.CharField(label='username', max_length=50, required=True)
    password = forms.CharField(label='password', max_length=50, required=True)   

    def save(self):           

class Map(forms.Form):
    buisnessName = forms.CharField(label='businessName', max_length=30, required=True)
    zipCode = forms.IntegersField(label='zipCode', max_length=5)
    city = forms.CharField(label='city', max_length=15)
    state = forms.CharField(label='state', max_length=18)

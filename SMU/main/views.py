from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer

from django.views.generic.edit import FormView
from django.views.generic import ListView

from django.shortcuts import render
from main.models import *


class Home(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'

    def get(self, request):
        queryset = User.objects.all()
        return Response({'user': queryset})
        
class Profile(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'pages/profile.html'

    def get(self, request):
        user = User.objects.all()
        return Response({'user': user})

from django.conf.urls import url, include
from django.contrib.auth import views
from django.contrib.auth.decorators import login_required, permission_required

from app.views import *

urlpatterns = [
    url(r'^$', Home.as_view(), name='index')
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', login_required(views.logout), {'next_page': 'base'}),
]
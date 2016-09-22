from django.http import HttpResponse
from django.template import loader
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
]
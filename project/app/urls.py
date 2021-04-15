from django.conf.urls import url, include
from django.contrib import admin
from . import views
urlpatterns = [
    url('about', views.about, name='about'),
    url('services', views.services, name='services'),
    url('contact', views.contact, name='contact'),
    url('', views.index, name='index')
]
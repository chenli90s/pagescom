from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('home', home),
    path('about', about),
    path('service', service),
    path('product.<cate>', product),
    path('contact', contact),
    path('login', login),
    path('register', register),
    path('detail.<name>', detail),
]
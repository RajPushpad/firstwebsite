from django.contrib import admin
from django.urls import path
from adidasapp import views

urlpatterns = [
    path("", views.index, name='adidasapp'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact')
]


    

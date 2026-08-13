from django.contrib import admin
from django.urls import path
from segundapp import views
urlpatterns = [
    path('primera/',views.inicio),
    path('hola/',views.saludo)
]

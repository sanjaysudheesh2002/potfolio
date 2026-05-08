
from django.contrib import admin
from django.urls import include, path

from myapp import views

urlpatterns = [
    path('home/',views.home_get),
    
]

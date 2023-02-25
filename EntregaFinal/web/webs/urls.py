from django.contrib import admin
from django.urls import path
from . import views

app_name="webs"
urlpatterns=  [ 
    path("", views.index, name="mi_web"),
]
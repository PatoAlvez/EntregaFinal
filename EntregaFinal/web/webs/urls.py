from django.contrib import admin
from django.urls import path
from webs import views
from django.contrib.auth.views import LogoutView

app_name="webs"
urlpatterns=  [ 
    path("", views.index, name="mi_web"),
    path("inicio", views.inicio, name="Inicio"),
    path("login", views.login_request, name="Login"),
    #path("logout", LogoutView.as_view, template_name= "webs/logout.html", name="Logout"),
]
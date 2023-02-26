from django.shortcuts import render, redirect
from .forms import RegistrarUsuarios
from .models import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    mis_usuarios = Usuarios.objects.all()
    if request.method == "POST":
        register_form= RegistrarUsuarios(request.POST)
        if register_form.is_valid():
            success=register_form.registrar_usuarios(request.user)
            return redirect("./")
    else:
        register_form=RegistrarUsuarios()
        return render(request, "webs/mi_web.html", {'register_form': register_form,'usuarios': mis_usuarios}, {"Mensaje":"Usuario creado"})
    
def BaseDeDatos(request):
    game= Juegos.objects.all()
    contexto= {"Juego:":game}
    return render(request, "webs/BaseDeDatos.html", contexto)
    
def eliminardatos(request, datos__nombre):
    game= Juegos.objects.get(nombre=datos__nombre)
    game.delete()

    game= Juegos.objects.all()
    contexto= {"Juego:":game}
    return render(request, "webs/BaseDeDatos.html", contexto)

def login_request(request):
    if request.method == "POST":
       form= AuthenticationForm(request, data= request.POST)
       if form.is_valid:
            usuario= form.cleaned_data.get("Username")
            contraseña= form.cleaned_data.get("Password")
            user= authenticate(username=usuario, password=contraseña)
            if user is not None:
                login(request, user)
                return render(request,"webs/inicio.html", {"Mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request,"webs/inicio.html", {"Mensaje":"Error, datos incorrectos"})
    else:
        return render(request,"webs/inicio.html", {"Mensaje":"Error"})
    
    form= AuthenticationForm()
    return render(request,"webs/login.html", {"form": form} )


def inicio(request):
    return render(request, "webs/inicio.html")
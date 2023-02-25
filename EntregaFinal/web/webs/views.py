from django.shortcuts import render, redirect
from .forms import RegistrarUsuarios
from .models import Usuarios
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
        return render(request, "webs/mi_web.html", {'register_form': register_form,'usuarios': mis_usuarios})
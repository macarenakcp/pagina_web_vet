from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Mascota
from .forms import MascotaForm

#estas son las diferentes vistas a las que accede el usuario

def inicio(request):
    return render(request, "paginas/inicio.html")

def nosotros(request):
    return render(request, "paginas/nosotros.html")

def listado(request):
    mascotas = Mascota.objects.all()
    return render(request, "vet/index.html", {"mascotas": mascotas})

def eliminar(request, mascota_id):
    mascota = Mascota.objects.get(id= mascota_id)
    mascota.delete()
    return redirect('vet')

def crear(request):
    formulario = MascotaForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('vet')
    return render(request, "vet/crear.html", {"formulario": formulario})
    
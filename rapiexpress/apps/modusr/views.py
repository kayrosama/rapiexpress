from django.shortcuts import render, redirect
from django.http import HttpResponse

#import apps.modusr
from .models import Usuarios
from .forms import UserForm

# Create your views here.
def inicio(request):
    return HttpResponse("<h1>Bienvenido a mi mundo</h1>")

def nosotros(request):
    return render(request, "paginas/nosotros.html")

def rapiexpress(request):
    Clientes = Usuarios.objects.all()
    return render(request, "paginas/rapiexpress.html", {'Clientes':Clientes})

def crear(request):
    return render(request, "paginas/crear.html")

def crear(request):
    formulario = UserForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('entrada')
    return render(request, 'paginas/crear.html', {'formulario':formulario})

def editar(request, id):
    libro = Usuarios.objects.get(id=id)
    formulario = UserForm(request.POST or None, request.FILES or None, instance=libro)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('entrada')
    return render(request, 'paginas/editar.html', {'formulario':formulario})

def eliminar(request, id):
    libro = Usuarios.objects.get(id=id)
    libro.delete()
    return redirect('entrada')

def login(request):
    return render(request, "paginas/xlogin.html")

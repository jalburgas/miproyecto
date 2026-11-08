from django.shortcuts import render
from .models import Articulo


def inicio(request):
    return render(request, 'blog/inicio.html')


def lista_articulos(request):
    articulos = Articulo.objects.all().order_by('-creado')
    return render(request, 'blog/lista.html', {'articulos': articulos})
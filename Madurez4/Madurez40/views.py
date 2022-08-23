from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return render(request, 'paginas/Inicio.html')

def tercera(request):
    return render(request, 'paginas/Tercera.html')
    
# Create your views here.

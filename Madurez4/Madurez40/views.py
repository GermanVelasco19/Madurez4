from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return render(request, 'paginas/Inicio.html')

def tercera(request):
    return render(request, 'paginas/Tercera.html')
    
def Quinta(request):
    return render(request, 'paginas/Quinta.html')

def Septima(request):
    return render(request, 'paginas/Septima.html')
# Create your views here.

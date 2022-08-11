from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return render(request, 'Madurez40/inicio.html')
    
# Create your views here.

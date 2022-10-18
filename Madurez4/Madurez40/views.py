from decimal import Context
from urllib.request import Request
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from Madurez40.models import Empresa
from django.http import JsonResponse
from django.views import View

def inicio(request):
    return render(request, 'paginas/Inicio.html')

def segunda(request):
    return render(request,'paginas/segunda.html')

def tercera(request):
    return render(request, 'paginas/Tercera.html')

def Cuarta(request):
    return render(request, 'paginas/cuarta.html')
    
def Quinta(request):
    return render(request, 'paginas/Quinta.html')

def Sexta(request):
    return render(request, 'paginas/sexta.html')

def Septima(request):
    return render(request, 'paginas/Septima.html')

def octava(request) :
    return render(request, 'paginas/octava.html')

def Novena(request):
    return render(request, 'paginas/Novena.html')

def Decima(request):
    return render(request, 'paginas/decima.html')

def Onceava(request):
    return render(request, 'paginas/Onceava.html')

def Doceava(request):
    return render(request, 'paginas/Doceava.html')

def Treceava(request):
    return render(request, 'paginas/Treceava.html')
# Create your views here.

def Catorce(request):
    return render(request, 'paginas/catorce.html/')

def verResumen(request,NombreCompleto,nombreEmpresa,Cargo,TipodeIndustria,tamañodeEmpresa,Telefono,Correo,reto1,reto2,Dimension11,Dimension12,Dimension21,Dimension22,Dimension31,Dimension32,Dimension33,Dimension34,Dimension35,Dimension36,Dimension37,Dimension38,NivelIngresos,CostoDirectoComoPorcentaje,CostoDirecto,valorInventario):
    empresa=Empresa.create(NombreCompleto,nombreEmpresa,Cargo,TipodeIndustria,tamañodeEmpresa,Telefono,Correo,reto1,reto2,Dimension11,Dimension12,Dimension21,Dimension22,Dimension31,Dimension32,Dimension33,Dimension34,Dimension35,Dimension36,Dimension37,Dimension38,NivelIngresos,CostoDirectoComoPorcentaje,CostoDirecto,valorInventario)
    
    return render(request, 'paginas/catorce.html')

class EmpresasView(View):
    def get(self, request):
        empresas = Empresa.objects.values()
        if len(empresas) > 0:
            return JsonResponse(list(empresas), safe=False)
        else:
            return JsonResponse({"message": "No hay empresas"}, status=404)

    


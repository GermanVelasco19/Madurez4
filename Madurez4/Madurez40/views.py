from decimal import Context
from multiprocessing import context
from urllib.request import Request
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from Madurez40.models import Empresa
from django.http import JsonResponse
from django.views import View
import matplotlib.pyplot as plt

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
    return render(request, 'paginas/catorce.html')

def Resultados(request,NombreCompleto,nombreEmpresa,Cargo,TipodeIndustria,tamañodeEmpresa,Telefono,Correo,reto1,reto2,Dimension11,Dimension12,Dimension21,Dimension22,Dimension31,Dimension32,Dimension33,Dimension34,Dimension35,Dimension36,Dimension37,Dimension38,NivelIngresos,CostoDirectoComoPorcentaje,CostoDirecto,valorInventario):
    empresa=Empresa.create(NombreCompleto,nombreEmpresa,Cargo,TipodeIndustria,tamañodeEmpresa,Telefono,Correo,reto1,reto2,Dimension11,Dimension12,Dimension21,Dimension22,Dimension31,Dimension32,Dimension33,Dimension34,Dimension35,Dimension36,Dimension37,Dimension38,NivelIngresos,CostoDirectoComoPorcentaje,CostoDirecto,valorInventario)
    return resultados(request,NombreCompleto)
    

class EmpresasView(View):
    def get(self, request):
        empresas = Empresa.objects.values()
        if len(empresas) > 0:
            return JsonResponse(list(empresas), safe=False)
        else:
            return JsonResponse({"message": "No hay empresas"}, status=404)

    
def resultados(request,NombreCompleto):
    empresa=Empresa.objects.get(nombreCompleto=NombreCompleto)
    tipo = empresa.TipodeIndustria
    pares= Empresa.objects.filter(TipodeIndustria=tipo)
    promedioDimension1=[]
    promedioDimension2=[]
    promedioDimension3=[]
    for i in pares:
        promedioDimension1.append((i.Dimension11+i.Dimension12)/2)
        promedioDimension2.append((i.Dimension21+i.Dimension22)/2)
        promedioDimension3.append((i.Dimension31+i.Dimension32+i.Dimension33+i.Dimension34+i.Dimension35+i.Dimension36+i.Dimension37+i.Dimension38)/8)
    
    Dimension1=sum(promedioDimension1)/len(promedioDimension1)
    Dimension2=sum(promedioDimension2)/len(promedioDimension2)
    Dimension3=sum(promedioDimension3)/len(promedioDimension3)

    nivelActual=[(empresa.Dimension11+empresa.Dimension12)/2,(empresa.Dimension21+empresa.Dimension22)/2,(empresa.Dimension31+empresa.Dimension32+empresa.Dimension33+empresa.Dimension34+empresa.Dimension35+empresa.Dimension36+empresa.Dimension37+empresa.Dimension38)/8]
    Dimension1Comparado=0
    Dimension2Comparado=0
    Dimension3Comparado=0

    if nivelActual[0]>Dimension1:
        Dimension1Comparado=1
    elif nivelActual[0]<Dimension1:
        Dimension1Comparado=-1
    else:
        Dimension1Comparado=0

    if nivelActual[1]>Dimension2:
        Dimension2Comparado=1   
    elif nivelActual[1]<Dimension2:
        Dimension2Comparado=-1
    else:
        Dimension2Comparado=0

    if nivelActual[2]>Dimension3:
        Dimension3Comparado=1
    elif nivelActual[2]<Dimension3:
        Dimension3Comparado=-1
    else:
        Dimension3Comparado=0
    nivelMadurez=''

    if Dimension1Comparado ==1 and Dimension2Comparado==1 and Dimension3Comparado==1:
        nivelMadurez="Mejores que parez"
    elif Dimension1Comparado ==0 and Dimension2Comparado==0 and Dimension3Comparado==0:
        nivelMadurez="Igual que parez"
    elif Dimension1Comparado ==-1 and Dimension2Comparado==-1 and Dimension3Comparado==-1:
        nivelMadurez="Peores que parez"
    else:
        nivelMadurez="En algunas dimension mejor que parez y en otras peor"
    
    ImplementacionEstrategiaTransformacion=[0.03,0.02,0.01,0]
    CulturaDigital=[0.03,0.02,0.01,0]
    PlaneacionDeDemanda=[0.1,0.05,0.03,0]
    Posicionamiento_Branding=[0.15,0.1,0.05,0]
    Proceso_productivo=[0.6,0.4,0.2,0]
    Generacion_de_Datos=[0.05,0.03,0.02,0]
    Trazabilidad=[0.06,0.04,0.02,0]
    Indicadores=[0.08,0.04,0.02,0]
    Control_Operaciones=[0.08,0.04,0.02,0]
    Seguridad=[0.04,0.02,0.01,0]

    AumentarIngresosmin=0.02
    AumentarIngresosmax=0.20
    AumentarIngresos=0
    BajarCostoProduccionmin=0.05
    BajarCostoProduccionmax=0.30
    BajarCostoProduccion=0
    AhorroMaterialesmin=0.05
    AhorroMaterialesmax=0.30
    AhorroMateriales=0
    AhorroManoObramin=0.05
    AhorroManoObramax=0.20
    AhorroManoObra=0
    AhorroServTercerosmin=0.05
    AhorroServTercerosmax=0.20
    AhorroServTerceros=0
    AhorroServPublicosmin=0.01
    AhorroServPublicosmax=0.05
    AhorroServPublicos=0
    BajarCostoLogisticamin=0
    BajarCostoLogisticamax=0.5
    BajarCostoLogistica=0

    AumentarIngresos=ImplementacionEstrategiaTransformacion[empresa.Dimension11-1]+PlaneacionDeDemanda[empresa.Dimension21-1]+Posicionamiento_Branding[empresa.Dimension22-1]+Trazabilidad[empresa.Dimension33-1]
    BajarCostoProduccion=CulturaDigital[empresa.Dimension12-1]+Generacion_de_Datos[empresa.Dimension32-1]+Control_Operaciones[empresa.Dimension35-1]
    AhorroMateriales=Indicadores[empresa.Dimension34-1]
    AhorroManoObra=Proceso_productivo[empresa.Dimension31-1]+Seguridad[empresa.Dimension36-1]
    AhorroServTerceros=0
    AhorroServPublicos=0
    BajarCostoLogistica=0

    if AumentarIngresos<AumentarIngresosmin:
        AumentarIngresos=AumentarIngresosmin
    elif AumentarIngresos>AumentarIngresosmax:
        AumentarIngresos=AumentarIngresosmax

    if BajarCostoProduccion<BajarCostoProduccionmin:
        BajarCostoProduccion=BajarCostoProduccionmin
    elif BajarCostoProduccion>BajarCostoProduccionmax:
        BajarCostoProduccion=BajarCostoProduccionmax
    
    if AhorroMateriales<AhorroMaterialesmin:
        AhorroMateriales=AhorroMaterialesmin
    elif AhorroMateriales>AhorroMaterialesmax:
        AhorroMateriales=AhorroMaterialesmax

    if AhorroManoObra<AhorroManoObramin:
        AhorroManoObra=AhorroManoObramin
    elif AhorroManoObra>AhorroManoObramax:
        AhorroManoObra=AhorroManoObramax

    if AhorroServTerceros<AhorroServTercerosmin:
        AhorroServTerceros=AhorroServTercerosmin
    elif AhorroServTerceros>AhorroServTercerosmax:
        AhorroServTerceros=AhorroServTercerosmax

    if AhorroServPublicos<AhorroServPublicosmin:
        AhorroServPublicos=AhorroServPublicosmin
    elif AhorroServPublicos>AhorroServPublicosmax:
        AhorroServPublicos=AhorroServPublicosmax

    if BajarCostoLogistica<BajarCostoLogisticamin:
        BajarCostoLogistica=BajarCostoLogisticamin
    elif BajarCostoLogistica>BajarCostoLogisticamax:
        BajarCostoLogistica=BajarCostoLogisticamax


    context = {
        'Compania':empresa.nombreEmpresa,
        'Actual':round((nivelActual[0]+nivelActual[1]+nivelActual[2])/3,1),
        'Sector':round((Dimension1+Dimension2+Dimension3)/3,1),
        'Correo':empresa.Correo

    }

    return render(request,'paginas/Resultados.html', context=context)

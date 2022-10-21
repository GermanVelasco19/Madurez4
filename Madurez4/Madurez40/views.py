from decimal import Context
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
    return render(request, 'paginas/catorce.html/')

def verResumen(request,NombreCompleto,nombreEmpresa,Cargo,TipodeIndustria,tamañodeEmpresa,Telefono,Correo,reto1,reto2,Dimension11,Dimension12,Dimension21,Dimension22,Dimension31,Dimension32,Dimension33,Dimension34,Dimension35,Dimension36,Dimension37,Dimension38,NivelIngresos,CostoDirectoComoPorcentaje,CostoDirecto,valorInventario):
    empresa=Empresa.create(NombreCompleto,nombreEmpresa,Cargo,TipodeIndustria,tamañodeEmpresa,Telefono,Correo,reto1,reto2,Dimension11,Dimension12,Dimension21,Dimension22,Dimension31,Dimension32,Dimension33,Dimension34,Dimension35,Dimension36,Dimension37,Dimension38,NivelIngresos,CostoDirectoComoPorcentaje,CostoDirecto,valorInventario)
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


    

    contenido="""
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
    </head>
    <body>
        <center><h1>Resultados</h1></center>
        <h2>Nombre Completo: {}</h2>
        <h2>Nombre de la empresa: {}</h2>
        <h2>Tipo de industria a la que pertenece: {}</h2>
        <h2>Nivel actual de madurez: </h2>
            <h3>Dimension 1: {}</h3>
            <h3>Dimension 2: {}</h3>
            <h3>Dimension 3: {}</h3>
        <h2>Nivel de madurez de parez: </h2>
            <h3>Dimension 1: {}</h3>
            <h3>Dimension 2: {}</h3>
            <h3>Dimension 3: {}</h3>
        <h2>Comparacion: </h2>
            <h3>Dimension 1: {}</h3>
            <h3>Dimension 2: {}</h3>
            <h3>Dimension 3: {}</h3>
        <table class="table table-striped" border="1">
            <tr>
                <td>Tipo de potencial</td>
                <td>Porcentaje</td>
                <td>COP a COP por anio</td>
            </tr>
            <tr>
                <td>Aumentar Ingresos/Ventas</td>
                <td>{}%</td>
                <td>{}</td>
            </tr>
            <tr>
                <td>Bajar costo de produccion</td>
                <td>{}%</td>
                <td>{}</td>
            </tr>
            <tr>
                <td>Ahorro en materiales/materia prima</td>
                <td>{}%</td>
                <td>{}</td>
            </tr>
            <tr>
                <td>Ahorrar en mano de obra</td>
                <td>{}%</td>
                <td>{}</td>
            </tr>
            <tr>
                <td>Ahorro en servicios de terceros & Mantenimiento</td>
                <td>{}%</td>
                <td>{}</td>
            </tr>
            <tr>
                <td>Ahorro en servicios publicos: Electricidad,Combustible,Gas,etc.</td>
                <td>{}%</td>
                <td>{}</td>
            </tr>
            <tr>
                <td>Bajar costo de logistica & inventario</td>
                <td>{}%</td>
                <td>{}</td>
            </tr>
        </table>

        <h2> Retos escogidos por la empresa: </h2>
        <h3> Reto1: {}</h3>
        <h3> Reto2: {}</h3>
    </body>

    """.format(empresa.nombreCompleto,empresa.nombreEmpresa,empresa.TipodeIndustria,nivelActual[0],nivelActual[1],nivelActual[2],Dimension1,Dimension2,Dimension3,nivelMadurez,nivelMadurez,nivelMadurez,AumentarIngresos*100,AumentarIngresos*empresa.NivelIngresos,BajarCostoProduccion*100,BajarCostoProduccion*empresa.NivelIngresos,AhorroMateriales*100,AhorroMateriales*empresa.NivelIngresos,AhorroManoObra*100,empresa.NivelIngresos,AhorroServTerceros*100,AhorroServTerceros*empresa.NivelIngresos,AhorroServPublicos*100,AhorroServPublicos*empresa.NivelIngresos,BajarCostoLogistica*100,BajarCostoLogistica*empresa.NivelIngresos,empresa.reto1,empresa.reto2)

    return HttpResponse(contenido) 

def details(request,nombreCompleto):
    empresa=Empresa.objects.get(nombreCompleto=nombreCompleto)

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


    

    contenido="""
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="../static/diseno.css">
    </head>
    <body>
        <h1 class="H1Resultados">Resultados</h1>
        <h2>Nombre Completo: {}</h2>
        <h2>Nombre de la empresa: {}</h2>
        <h2>Tipo de industria a la que pertenece: {}</h2>
        <h2>Nivel actual de madurez: </h2>
            <h3>Dimension 1: {}</h3>
            <h3>Dimension 2: {}</h3>
            <h3>Dimension 3: {}</h3>
        <h2>Nivel de madurez de parez: </h2>
            <h3>Dimension 1: {}</h3>
            <h3>Dimension 2: {}</h3>
            <h3>Dimension 3: {}</h3>
        <h2>Comparacion: </h2>
            <h3>Dimension 1: {}</h3>
            <h3>Dimension 2: {}</h3>
            <h3>Dimension 3: {}</h3>
        <table class="table table-striped" border="1">
            <tr>
                <td>Tipo de potencial</td>
                <td>Porcentaje</td>
                <td>COP a COP por anio</td>
            </tr>
            <tr>
                <td>Aumentar Ingresos/Ventas</td>
                <td>{}%</td>
                <td>{}</td>
            </tr>
            <tr>
                <td>Bajar costo de produccion</td>
                <td>{}%</td>
                <td>{}</td>
            </tr>
            <tr>
                <td>Ahorro en materiales/materia prima</td>
                <td>{}%</td>
                <td>{}</td>
            </tr>
            <tr>
                <td>Ahorrar en mano de obra</td>
                <td>{}%</td>
                <td>{}</td>
            </tr>
            <tr>
                <td>Ahorro en servicios de terceros & Mantenimiento</td>
                <td>{}%</td>
                <td>{}</td>
            </tr>
            <tr>
                <td>Ahorro en servicios publicos: Electricidad,Combustible,Gas,etc.</td>
                <td>{}%</td>
                <td>{}</td>
            </tr>
            <tr>
                <td>Bajar costo de logistica & inventario</td>
                <td>{}%</td>
                <td>{}</td>
            </tr>
        </table>

        <h2> Retos escogidos por la empresa: </h2>
        <h3> Reto1: {}</h3>
        <h3> Reto2: {}</h3>
    </body>

    """.format(empresa.nombreCompleto,empresa.nombreEmpresa,empresa.TipodeIndustria,nivelActual[0],nivelActual[1],nivelActual[2],Dimension1,Dimension2,Dimension3,nivelMadurez,nivelMadurez,nivelMadurez,AumentarIngresos*100,AumentarIngresos*empresa.NivelIngresos,BajarCostoProduccion*100,BajarCostoProduccion*empresa.NivelIngresos,AhorroMateriales*100,AhorroMateriales*empresa.NivelIngresos,AhorroManoObra*100,empresa.NivelIngresos,AhorroServTerceros*100,AhorroServTerceros*empresa.NivelIngresos,AhorroServPublicos*100,AhorroServPublicos*empresa.NivelIngresos,BajarCostoLogistica*100,BajarCostoLogistica*empresa.NivelIngresos,empresa.reto1,empresa.reto2)

    return HttpResponse(contenido) 


class EmpresasView(View):
    def get(self, request):
        empresas = Empresa.objects.values()
        if len(empresas) > 0:
            return JsonResponse(list(empresas), safe=False)
        else:
            return JsonResponse({"message": "No hay empresas"}, status=404)

    


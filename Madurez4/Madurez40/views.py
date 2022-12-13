from decimal import Context
from multiprocessing import context  # type: ignore
from urllib.request import Request
from xml.dom.minidom import Document
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from Madurez40.models import Empresa
from django.http import JsonResponse
from django.views import View
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django_xhtml2pdf.utils import pisa
from io import StringIO
from reportlab.pdfgen import canvas
import math

tipo=""
retos=["Mejorar Eficiencia Operacional en general",
        "Predicción de eventos críticos o fallas y/o Mantenimiento predictivo",
        "Tener información del proceso productivo para optimizar la planeación y los niveles de cumplimiento al cliente",
        "Reducir el consumo de Servicios Públicos: Energia, Agua, Combustible, Gas, etc",
        "Tener información real (costo unitario, insumos usados) y trazabilidad del producto para Terceros, Reguladores, Clientes",
        "Poder personalizar el producto final para cada cliente y/o reducir el tamaño mínimo de un lote de producción",
        "Reducir inventarios de producto final y/o materia prima",
        "Optimizar el uso del recuso humano, al eliminar tareas de poco valor (Ej.: Digitalización de información, robotización)",
        "Aumentar los niveles de Seguridad y Salud en el trabajo - Cero Accidentes"
        ]
    
proyectos=[
        "Mejorar la Eficiencia Operacional mediante la digitalización de la información de piso planta y la optimización de los procesos",
        "Aumentar el Run-Time de los activos mediante software y modelos de Analítica Predictiva",
        "Controlar los procesos productivos mediante la digitalización de los flujos de información del piso planta",
        "Medir, analizar y optimizar el consumo de servicios públicos",
        "Generar trazabilidad sobre los lotes de producción para asegurar el cumplimiento de normas y estándares de producción",
        "Habilitar la producción de productos personalizados ",
        "Disminuir los inventarios, al implementar un software y modelo tipo Demand-driven Material Requirements Planning",
        "Eliminar tareas manuales mediante la digitalización de rutinas, formularios o actividades manuales de captura de datos",
        "Accidentalidad 0.0 con tecnologías 4.0 en los procesos y los diferentes puntos de control de la producción"
    ]

impactos=[
        "Aumento OEE",
        "Reducir occurencia de eventos criticos",
        "Aumentar niveles de satisfacción y lealdad de clientes",
        "Ahorro",
        "Agilizar procesos de inspecciones, auditorias, certificaciones y agilizar eventos del tipo Product recall",
        "Aumentar Ventas",
        "Reducir Costo inventario",
        "Reducir tareas manuales y mano de obra requerida",
        "Reducir accidentalidad y bajar tasas de ausentismo"
    ]
cantidadesImpacto=[
        "2-5%",
        "40%",
        "25%",
        "10%",
        "-50%",
        "5%",
        "30%",
        "80%",
        "15%"
    ]

duracionesMin=[
        4,
        6,
        6,
        3,
        6,
        9,
        9,
        3,
        6
    ]

duracionesMax=[
        6,
        9,
        9,
        4,
        9,
        12,
        12,
        4,
        9
    ]

costosMin=[
        60,
        80,
        120,
        40,
        120,
        240,
        240,
        40,
        80
    ]

costosMax=[
        80,
        120,
        180,
        60,
        180,
        300,
        300,
        60,
        120
    ]

amortizacionesMin=[ 
        6,
        12,
        18,
        6,
        18,
        24,
        24,
        12,
        12
    ]

amortizacionesMax=[
        9,
        15,
        24,
        9,
        24,
        36,
        36,
        15,
        15
    ]

def inicio(request):
    return render(request, 'paginas/Inicio.html')

def segunda(request):
    return render(request,'paginas/segunda.html')

def tercera(request):
    return render(request, 'paginas/Tercera.html')

def Cuarta(request,TipoInustria):
    global tipo
    tipo=TipoInustria
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
    global tipo
    empresas = Empresa.objects.filter(TipodeIndustria=tipo)
    OtroCostoDirecto=0
    valorInv=0
    Costo=0
    Ingreso=0

    print(tipo)
    for i in empresas:
        valorInv+=i.valorInventario
        OtroCostoDirecto+=i.CostoDirecto
        Costo+=i.CostoDirectoComoPorcentaje
        Ingreso+=i.NivelIngresos
    
    if len(empresas)>0:
        valorInv=valorInv/len(empresas)
        OtroCostoDirecto=OtroCostoDirecto/len(empresas)
        Costo=Costo/len(empresas)
        Ingreso=Ingreso/len(empresas)
        
    millones=round(Ingreso/1000000)
    miles=round((Ingreso-millones*1000000)/1000)
    if miles<99:
        if miles<9:
            milesS="00"+str(miles)
        else:
            milesS="0"+str(miles)
    else:
        milesS=str(miles)
    unidades=round(Ingreso-millones*1000000-miles*1000)
    if unidades<99:
        if unidades<9:
            unidadesS="00"+str(unidades)
        else:
            unidadesS="0"+str(unidades)
    else:
        unidadesS=str(unidades)

    IngresoParaMostrar="{}.{}.{} COP".format(millones,milesS,unidadesS)
    context={
        'ValordeInv':round(100*valorInv),
        'CostoDirecto':round(OtroCostoDirecto),
        'CostoDComoPorcentaje':round(100*Costo),
        'Ingreso':round(Ingreso),
        'IngresoParaMostrar':IngresoParaMostrar
    }
    
    return render(request, 'paginas/Treceava.html', context=context)
# Create your views here.

def Catorce(request):
    return render(request, 'paginas/catorce.html')

def Resultados(request,NombreCompleto,nombreEmpresa,Cargo,TipodeIndustria,tamañodeEmpresa,Telefono,Correo,reto1,reto2,Dimension11,Dimension12,Dimension21,Dimension22,Dimension31,Dimension32,Dimension33,Dimension34,Dimension35,Dimension36,NivelIngresos,CostoDirectoComoPorcentaje,CostoDirecto,valorInventario):
   
    empresa=Empresa.create(NombreCompleto,nombreEmpresa,Cargo,TipodeIndustria,tamañodeEmpresa,Telefono,Correo,reto1,reto2,Dimension11,Dimension12,Dimension21,Dimension22,Dimension31,Dimension32,Dimension33,Dimension34,Dimension35,Dimension36,NivelIngresos,CostoDirectoComoPorcentaje,CostoDirecto,valorInventario)
    return resultados(request,NombreCompleto)
    
def informe(request):
    return render(request, 'paginas/Informe.html')
    

class EmpresasView(View):  # type: ignore
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
        promedioDimension3.append((i.Dimension31+i.Dimension32+i.Dimension33+i.Dimension34+i.Dimension35+i.Dimension36)/6)
    
    Dimension1=sum(promedioDimension1)/len(promedioDimension1)
    Dimension2=sum(promedioDimension2)/len(promedioDimension2)
    Dimension3=sum(promedioDimension3)/len(promedioDimension3)

    nivelActual=[(empresa.Dimension11+empresa.Dimension12)/2,(empresa.Dimension21+empresa.Dimension22)/2,(empresa.Dimension31+empresa.Dimension32+empresa.Dimension33+empresa.Dimension34+empresa.Dimension35+empresa.Dimension36)/6]
    
    ImplementacionEstrategiaTransformacion=[0.03,0.02,0.01,0]
    PlaneacionDeDemanda=[0.1,0.05,0.03,0]
    Posicionamiento_Branding=[0.15,0.1,0.05,0]
    Trazabilidad=[0.06,0.04,0.02,0]

    AumentarIngresosmin=0.02
    AumentarIngresosmax=0.20
    AumentarIngresos=0

    AumentarIngresos=ImplementacionEstrategiaTransformacion[empresa.Dimension11-1]+PlaneacionDeDemanda[empresa.Dimension21-1]+Posicionamiento_Branding[empresa.Dimension22-1]+Trazabilidad[empresa.Dimension33-1]

    if AumentarIngresos<AumentarIngresosmin:
        AumentarIngresos=AumentarIngresosmin
    elif AumentarIngresos>AumentarIngresosmax:
        AumentarIngresos=AumentarIngresosmax

    if AumentarIngresos-(0.1*AumentarIngresos)>AumentarIngresosmin:
        min=  AumentarIngresos-(0.1*AumentarIngresos)
    else:
        min= AumentarIngresosmin

    if AumentarIngresos+(0.1*AumentarIngresos)<AumentarIngresosmax:
        max=AumentarIngresos+(0.1*AumentarIngresos)
    else:
        max= AumentarIngresosmax
    minRango=round(min*100)
    maxRango=round(max*100)

    min=min*empresa.NivelIngresos
    max=max*empresa.NivelIngresos

    AumentarIngresosMostrarMin=''
    millones=math.trunc(min/1000000)
    miles=math.trunc((min-millones*1000000)/1000)
    if miles <99:
        if miles<9:
            milesS='00'+str(miles)
        else:
            milesS='0'+str(miles)
    else:
        milesS=str(miles)
    unidades=math.trunc(min-millones*1000000-miles*1000)
    if (unidades<99):
        if unidades<9:
            unidadesS='00'+str(unidades)
        else:
            unidadesS='0'+str(unidades)
    else:
        unidadesS=str(unidades)
    
    if millones>0:
        AumentarIngresosMostrarMin=str(millones)+','+milesS+','+unidadesS+' COP'
    else:
        if miles>0:
            AumentarIngresosMostrarMin=str(miles)+','+unidadesS+' COP'
        else:
            AumentarIngresosMostrarMin=str(unidades)+' COP'
    
    AumentarIngresosMostrarMax=''
    millones=math.trunc(max/1000000)
    miles=math.trunc((max-millones*1000000)/1000)
    if miles <99:
        if miles<9:
            milesS='00'+str(miles)
        else:
            milesS='0'+str(miles)
    else:
        milesS=str(miles)
    unidades=math.trunc(max-millones*1000000-miles*1000)
    if (unidades<99):
        if unidades<9:
            unidadesS='00'+str(unidades)
        else:
            unidadesS='0'+str(unidades)
    else:
        unidadesS=str(unidades)
    
    if millones>0:
        AumentarIngresosMostrarMax=str(millones)+','+milesS+','+unidadesS+' COP'
    else:
        if miles>0:
            AumentarIngresosMostrarMax=str(miles)+','+unidadesS+' COP'
        else:
            AumentarIngresosMostrarMax=str(unidades)+' COP'

    mensaje=''
    if round(((nivelActual[0]+nivelActual[1]+nivelActual[2])/3),1)<=1.4:
        mensaje="Usted está iniciando su Transformación Digital de Operaciones. Las oportunidades y retos son casi infinitos y es importante saber priorizar."
    elif round(((nivelActual[0]+nivelActual[1]+nivelActual[2])/3),0)<=2.5:
        mensaje="Usted ya ha logrado sus primeros avances en la Transformación Digital de Operaciones. Estos logros iniciales generan validación y justificación de seguir adelante con la Ruta de Transformación."
    elif round(((nivelActual[0]+nivelActual[1]+nivelActual[2])/3),0)<=3.4:
        mensaje="Felicitaciones: Usted ya tiene un nivel avanzado en su Transformación Digital de Operaciones. Los retos seguramente estarán en el aprovechamiento de las inversiones realizadas."
    elif round(((nivelActual[0]+nivelActual[1]+nivelActual[2])/3),0)<=4.0:
        mensaje="Felicitaciones: Usted es un Líder Digital y pertenece al 2% de las empresas en Colombia que se caracterizan por el dinamismo continuo en sus Transformaciones Empresariales."

    proyecto1=''
    proyecto2=''

    proyecto1=proyectos[empresa.reto1-1]
    proyecto2=proyectos[empresa.reto2-1]

    proy=empresa.reto1-1
    impacto=impactos[proy]
    cantImpacto=cantidadesImpacto[proy]
    duracionMin=duracionesMin[proy]
    duracionMax=duracionesMax[proy]
    costoMin=costosMin[proy]
    costoMax=costosMax[proy]
    amortizacionMin=amortizacionesMin[proy]
    amortizacionMax=amortizacionesMax[proy]

    ParesConMismoReto=len(Empresa.objects.filter(reto1=empresa.reto1))/len(Empresa.objects.all())
    ParesConMismoReto2=len(Empresa.objects.filter(reto2=empresa.reto2))/len(Empresa.objects.all())

    context = {
        'Compania':empresa.nombreEmpresa,
        'Actual':round((nivelActual[0]+nivelActual[1]+nivelActual[2])/3,1),
        'Sector':round((Dimension1+Dimension2+Dimension3)/3,1),
        'Correo':empresa.Correo,
        'min':AumentarIngresosMostrarMin,
        'max':AumentarIngresosMostrarMax,
        'mensaje':mensaje,
        'proyecto1':proyecto1,
        'proyecto2':proyecto2,
        'impacto':impacto,
        'cantImpacto':cantImpacto,
        'minDuracion':duracionMin,
        'maxDuracion':duracionMax,
        'minCosto':costoMin,
        'maxCosto':costoMax,
        'minAmortizacion':amortizacionMin,
        'maxAmortizacion':amortizacionMax
    } 
    comparacion=0
    if (round((nivelActual[0]+nivelActual[1]+nivelActual[2])/3,1)==round((Dimension1+Dimension2+Dimension3)/3,1)):
        comparacion=0
    elif (round((nivelActual[0]+nivelActual[1]+nivelActual[2])/3,1)>round((Dimension1+Dimension2+Dimension3)/3,1)):
        comparacion=1
    else:
        comparacion=-1

    Informe(empresa,ParesConMismoReto,ParesConMismoReto2,comparacion,AumentarIngresosMostrarMin,AumentarIngresosMostrarMax,minRango,maxRango)
    return render(request,'paginas/Resultados.html', context=context)

def generar_PDF(html):
    result=open('informe.pdf','w+b')
    pisaStatus = pisa.CreatePDF(html, dest=result, encoding='utf-8')
    result.seek(0)
    pdf = result.read()
    result.close()
    return pdf

def Informe(empresa,ParesConMismoReto,ParesConMismoReto2,comparacion,min,max,minRango,maxRango):
    subject = 'Informe de Transformación Digital de Operaciones'
    proyecto1=proyectos[empresa.reto1-1]
    proyecto2=proyectos[empresa.reto2-1]
    template = get_template('paginas/Informe.html')

    texto = ''

    if comparacion == 1:
        texto = ' está por delante de su competencia en Colombia en relación a su Madurez Digital de Operaciones.'
    elif comparacion == -1:
        texto = ' está un paso atrás de su competencia en Colombia en relación a su Madurez Digital de Operaciones.'
    elif comparacion == 0:
        texto = ' está a la par con su competencia en Colombia en relación a la Madurez Digital de sus Operaciones.'

    content = template.render({
        'Nombre_empresa':empresa.nombreEmpresa,
        'cargo':empresa.Cargo,
        'Nombre_persona':empresa.nombreCompleto,
        'Reto1':retos[empresa.reto1-1],
        'Reto2':retos[empresa.reto2-1],
        'tamano':empresa.tamanodeEmpresa,
        'sector':empresa.TipodeIndustria,
        'MismoReto1':ParesConMismoReto*100,
        'MismoReto2':ParesConMismoReto2*100,
        'texto': texto,
        'minCOP':min,
        'maxCOP':max,
        'Impacto':'Aumentar ingresos',
        'minRango': minRango,
        'maxRango': maxRango,
        'proyecto1':proyecto1,
        'proyecto2':proyecto2
    })
    mensaje = '''Buen día {},
    <br><br>

Nos complace saber que Usted realizó el Auto-Diagnostico sobre el nivel de Madurez Digital en sus Operaciones. Adjuntamos un informe con los resultados de su empresas y con unas ideas y sugerencias para seguir adelante con la Transformación Digital. 
<br><br>
El informe tiene una evaluación comparativa de la situación actual de su empresas, las sugerencias para seguir adelante con la Digitalización de sus Operaciones, y algo muy importante: Una estimación de los potenciales beneficios para su empresa de la Digitalización de Operaciones.
<br><br>
Sería un gusto para nosotros poder profundizar y discutir estos resultados personalmente. Estamos a su disposición y quedamos atentos, cordial saludo
<br><br>
<br><br>
Andres Pinzón
'''.format(empresa.nombreCompleto)
    content=generar_PDF(content)
    message = EmailMultiAlternatives(subject=subject,from_email=settings.EMAIL_HOST_USER, to=[empresa.Correo])
    message.attach_alternative(mensaje, 'text/html')
    message.attach('informe.pdf',content, 'application/pdf')
    message.send()



class EmpresasView(View):
    def get(self, request):
        empresas = Empresa.objects.values()
        if len(empresas) > 0:
            return JsonResponse(list(empresas), safe=False)
        else:
            return JsonResponse({"message": "No hay empresas"}, status=404)

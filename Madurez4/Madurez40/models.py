from django.db import models

# Create your models here.
class retos(models.IntegerChoices):
    primero=1,'1',
    segundo=2,'2',
    tercero=3,'3',
    cuarto=4,'4',
    quinto=5,'5',
    sexto=6,'6',
    septimo=7,'7',
    octavo=8,'8',

class Dimension(models.IntegerChoices):
    primero=1,'1',
    segundo=2,'2',
    tercero=3,'3',
    cuarto=4,'4',

class Empresa(models.Model):
    nombreCompleto = models.CharField(max_length=500, primary_key=True)
    nombreEmpresa = models.CharField(max_length=500)
    Cargo = models.CharField(max_length=500)
    TipodeIndustria = models.CharField(max_length=500,default='Industria')
    tamañodeEmpresa = models.CharField(max_length=500,default='Tamaño de la empresa')
    Telefono = models.CharField(max_length=100,default='Telefono')
    Correo = models.EmailField(max_length=254)

    reto1 = models.IntegerField(choices=retos.choices, default=retos.primero)
    reto2 = models.IntegerField(choices=retos.choices, default=retos.segundo)

    Dimension11= models.IntegerField(choices=Dimension.choices, default=Dimension.primero)
    Dimension12= models.IntegerField(choices=Dimension.choices, default=Dimension.primero)  

    Dimension21= models.IntegerField(choices=Dimension.choices, default=Dimension.primero)
    Dimension22= models.IntegerField(choices=Dimension.choices, default=Dimension.primero)

    Dimension31= models.IntegerField(choices=Dimension.choices, default=Dimension.primero)
    Dimension32= models.IntegerField(choices=Dimension.choices, default=Dimension.primero)
    Dimension33= models.IntegerField(choices=Dimension.choices, default=Dimension.primero)
    Dimension34= models.IntegerField(choices=Dimension.choices, default=Dimension.primero)
    Dimension35= models.IntegerField(choices=Dimension.choices, default=Dimension.primero)
    Dimension36= models.IntegerField(choices=Dimension.choices, default=Dimension.primero)
    Dimension37= models.IntegerField(choices=Dimension.choices, default=Dimension.primero)
    Dimension38= models.IntegerField(choices=Dimension.choices, default=Dimension.primero)

    NivelIngresos= models.CharField(max_length=500,default='Nivel de ingresos')
    CostoDirectoComoPorcentaje=models.CharField(max_length=500,default='Costo directo como porcentaje')
    CostoDirecto=models.CharField(max_length=500,default='Costo directo')

    valorInventario = models.CharField(max_length=500,default='Valor de inventario')

    def __str__(self):
        return self.nombreCompleto
    
    def create(empresa):
        Empresa.nombreCompleto = empresa.nombreCompleto
        Empresa.nombreEmpresa = empresa.nombreEmpresa
        Empresa.Cargo = empresa.Cargo
        Empresa.TipodeIndustria = empresa.TipodeIndustria
        Empresa.tamañodeEmpresa = empresa.tamañodeEmpresa
        Empresa.Telefono = empresa.Telefono
        Empresa.Correo = empresa.Correo
        Empresa.reto1 = empresa.reto1
        Empresa.reto2 = empresa.reto2
        Empresa.Dimension11 = empresa.Dimension11
        Empresa.Dimension12 = empresa.Dimension12
        Empresa.Dimension21 = empresa.Dimension21
        Empresa.Dimension22 = empresa.Dimension22
        Empresa.Dimension31 = empresa.Dimension31
        Empresa.Dimension32 = empresa.Dimension32
        Empresa.Dimension33 = empresa.Dimension33
        Empresa.Dimension34 = empresa.Dimension34
        Empresa.Dimension35 = empresa.Dimension35
        Empresa.Dimension36 = empresa.Dimension36
        Empresa.Dimension37 = empresa.Dimension37
        Empresa.Dimension38 = empresa.Dimension38
        Empresa.NivelIngresos = empresa.NivelIngresos
        Empresa.CostoDirectoComoPorcentaje = empresa.CostoDirectoComoPorcentaje
        Empresa.CostoDirecto = empresa.CostoDirecto
        Empresa.valorInventario = empresa.valorInventario
        Empresa.save()
        return Empresa
        

    def create(NombreCompleto,nombreEmpresa,Cargo,TipodeIndustria,tamañodeEmpresa,Telefono,Correo,reto1,reto2,Dimension11,Dimension12,Dimension21,Dimension22,Dimension31,Dimension32,Dimension33,Dimension34,Dimension35,Dimension36,Dimension37,Dimension38,NivelIngresos,CostoDirectoComoPorcentaje,CostoDirecto,valorInventario):
        Empresa.nombreCompleto = NombreCompleto
        Empresa.nombreEmpresa = nombreEmpresa
        Empresa.Cargo = Cargo
        Empresa.TipodeIndustria = TipodeIndustria
        Empresa.tamañodeEmpresa = tamañodeEmpresa
        Empresa.Telefono = Telefono
        Empresa.Correo = Correo
        Empresa.reto1 = reto1
        Empresa.reto2 = reto2
        Empresa.Dimension11 = Dimension11
        Empresa.Dimension12 = Dimension12
        Empresa.Dimension21 = Dimension21
        Empresa.Dimension22 = Dimension22
        Empresa.Dimension31 = Dimension31
        Empresa.Dimension32 = Dimension32
        Empresa.Dimension33 = Dimension33
        Empresa.Dimension34 = Dimension34
        Empresa.Dimension35 = Dimension35
        Empresa.Dimension36 = Dimension36
        Empresa.Dimension37 = Dimension37
        Empresa.Dimension38 = Dimension38
        Empresa.NivelIngresos = NivelIngresos
        Empresa.CostoDirectoComoPorcentaje = CostoDirectoComoPorcentaje
        Empresa.CostoDirecto = CostoDirecto
        Empresa.valorInventario = valorInventario
        Empresa.save()

        return Empresa

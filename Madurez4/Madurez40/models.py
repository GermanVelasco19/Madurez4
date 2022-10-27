from django.db import models

# Create your models here.

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
    tamanodeEmpresa = models.CharField(max_length=500,default='Tamaño de la empresa')
    Telefono = models.CharField(max_length=100,default='Telefono')
    Correo = models.EmailField(max_length=254)

    reto1 = models.CharField(max_length=1000)
    reto2 = models.CharField(max_length=1000)

    Dimension11= models.PositiveIntegerField(default=1)
    Dimension12= models.PositiveIntegerField(default=1)

    Dimension21= models.PositiveIntegerField(default=1)
    Dimension22= models.PositiveIntegerField(default=1)

    Dimension31= models.PositiveIntegerField(default=1)
    Dimension32= models.PositiveIntegerField(default=1)
    Dimension33= models.PositiveIntegerField(default=1)
    Dimension34= models.PositiveIntegerField(default=1)
    Dimension35= models.PositiveIntegerField(default=1)
    Dimension36= models.PositiveIntegerField(default=1)
    Dimension37= models.PositiveIntegerField(default=1)
    Dimension38= models.PositiveIntegerField(default=1)

    NivelIngresos= models.FloatField(default=0)
    CostoDirectoComoPorcentaje=models.FloatField(default=0)
    CostoDirecto=models.FloatField(default=0)

    valorInventario = models.FloatField(default=0)

    def _init_(self):
        self.nombreCompleto = ''
        self.nombreEmpresa = ''
        self.Cargo = ''
        self.TipodeIndustria = ''
        self.tamanodeEmpresa = ''
        self.Telefono = ''
        self.Correo = ''
        self.reto1 = 1
        self.reto2 = 2
        self.Dimension11 = 1
        self.Dimension12 = 1
        self.Dimension21 = 1
        self.Dimension22 = 1
        self.Dimension31 = 1
        self.Dimension32 = 1
        self.Dimension33 = 1
        self.Dimension34 = 1
        self.Dimension35 = 1
        self.Dimension36 = 1
        self.Dimension37 = 1
        self.Dimension38 = 1
        self.NivelIngresos = 0
        self.CostoDirectoComoPorcentaje = 0
        self.CostoDirecto = 0
        self.valorInventario = 0

        return self
    
    def create():
        a = Empresa._init_()
        a = Empresa()
        return Empresa
        
    def create(NombreCompleto,nombreEmpresa,Cargo,TipodeIndustria,tamanodeEmpresa,Telefono,Correo,reto1,reto2,Dimension11,Dimension12,Dimension21,Dimension22,Dimension31,Dimension32,Dimension33,Dimension34,Dimension35,Dimension36,Dimension37,Dimension38,NivelIngresos,CostoDirectoComoPorcentaje,CostoDirecto,valorInventario):
        a = Empresa()
        a.nombreCompleto = NombreCompleto
        a.nombreEmpresa = nombreEmpresa
        a.TipodeIndustria = TipodeIndustria
        a.Cargo = Cargo
        a.tamanodeEmpresa = tamanodeEmpresa
        a.Telefono = Telefono
        a.Correo = Correo
        a.reto1 = reto1
        a.reto2 = reto2
        a.Dimension11 = Dimension11
        a.Dimension12 = Dimension12
        a.Dimension21 = Dimension21
        a.Dimension22 = Dimension22
        a.Dimension31 = Dimension31
        a.Dimension32 = Dimension32
        a.Dimension33 = Dimension33
        a.Dimension34 = Dimension34
        a.Dimension35 = Dimension35
        a.Dimension36 = Dimension36
        a.Dimension37 = Dimension37
        a.Dimension38 = Dimension38
        a.NivelIngresos = NivelIngresos
        a.CostoDirectoComoPorcentaje = CostoDirectoComoPorcentaje
        a.CostoDirecto = CostoDirecto
        a.valorInventario = valorInventario
        a.save()
        return a
        

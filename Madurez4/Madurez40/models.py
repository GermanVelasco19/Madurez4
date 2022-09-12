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

class Dimension1(models.IntegerChoices):
    primero=1,'1',
    segundo=2,'2',
    tercero=3,'3',
    cuarto=4,'4',

class Dimension2(models.IntegerChoices):
    primero=1,'1',
    segundo=2,'2',
    tercero=3,'3',
    cuarto=4,'4',

class Dimension3(models.IntegerChoices):
    primero=1,'1',
    segundo=2,'2',
    tercero=3,'3',
    cuarto=4,'4',

class NiveldeIngresos(models.IntegerChoices):
    uno = 1,'1',
    dos = 2,'2',
    tres = 3,'3',

class CostoDirectoComoPorcentaje(models.IntegerChoices):
    diez=10,'10',
    veinte=20,'20',
    treinta=30,'30',
    cuarenta=40,'40',
    cincuenta=50,'50',
    masdecincuenta=80,'80',

class valorInventario (models.IntegerChoices):
    menos =5,'5',
    entre11y30=20,'20',
    entre31y40=35,'35',
    entre41y50=45,'45',



class Empresa(models.Model):
    nombreCompleto = models.CharField(max_length=100, primary_key=True)
    nombreEmpresa = models.CharField(max_length=100)
    Cargo = models.CharField(max_length=100)
    TipodeIndustria = (
        ('Alimentación, bebida o prodcutos agroindustriales', 'Alimentación, bebida o prodcutos agroindustriales'),
        ('Textil, confección', 'Textil, confección'),
        ('Industria farmaceutica(laboratorios), Cosmética', 'Industria farmaceutica(laboratorios), Cosmética'),
        ('Consumer products', 'Consumer products'),
    )
    tamañodeEmpresa = (
        ('Pequeña (Hasta 10.000MCOP)', 'Pequeña (Hasta 10.000MCOP)'),
        ('Mediana (10.000MCOP - 100.000MCOP)', 'Mediana (10.000MCOP - 100.000MCOP)'),
        ('Grande (100.000MCOP - 1.000.000MCOP)', 'Grande (100.000MCOP - 1.000.000MCOP)'),
    )
    Telefono = models.CharField(max_length=100)
    Correo = models.CharField(max_length=100)

    reto1 = models.IntegerField(choices=retos.choices, default=retos.primero)
    reto2 = models.IntegerField(choices=retos.choices, default=retos.segundo)

    Dimension11= models.IntegerField(choices=Dimension1.choices, default=Dimension1.primero)
    Dimension12= models.IntegerField(choices=Dimension1.choices, default=Dimension1.segundo)  

    Dimension21= models.IntegerField(choices=Dimension2.choices, default=Dimension2.primero)
    Dimension22= models.IntegerField(choices=Dimension2.choices, default=Dimension2.segundo)

    Dimension31= models.IntegerField(choices=Dimension3.choices, default=Dimension3.primero)
    Dimension32= models.IntegerField(choices=Dimension3.choices, default=Dimension3.primero)
    Dimension33= models.IntegerField(choices=Dimension3.choices, default=Dimension3.primero)
    Dimension34= models.IntegerField(choices=Dimension3.choices, default=Dimension3.primero)
    Dimension35= models.IntegerField(choices=Dimension3.choices, default=Dimension3.primero)
    Dimension36= models.IntegerField(choices=Dimension3.choices, default=Dimension3.primero)
    Dimension37= models.IntegerField(choices=Dimension3.choices, default=Dimension3.primero)
    Dimension38= models.IntegerField(choices=Dimension3.choices, default=Dimension3.primero)

    Ingresos =[('1','1'),('2','2'),('3','3')]
    ValorInv =[('1','1'),('2','2'),('3','3'),('4','4')]

    NivelIngresos= models.IntegerField(choices=Ingresos, default=2)
    CostoDirectoComoPorcentaje=models.IntegerField(choices=CostoDirectoComoPorcentaje.choices, default=CostoDirectoComoPorcentaje.diez)
    CostoDirecto=models.BigIntegerField()

    valorInventario = models.IntegerField(choices=ValorInv, default=2)

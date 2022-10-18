from django.contrib import admin
from Madurez40.models import Empresa
import django_excel as excel 

# Register your models here.



class EmpresaAdmin(admin.ModelAdmin):
    actions=['descarga_empresas_csv']

    def descarga_empresas_csv(self,request,queryset):
        empresas = [['NombreCompleto','nombreEmpresa','Cargo','TipodeIndustria','tamanodeEmpresa','Telefono','Correo','reto1','reto2','Dimension11','Dimension12','Dimension21','Dimension22','Dimension31','Dimension32','Dimension33','Dimension34','Dimension35','Dimension36','Dimension37','Dimension38','NivelIngresos','CostoDirectoComoPorcentaje','CostoDirecto','valorInventario']]
        for empresa in queryset:
            empresas.append([empresa.nombreCompleto,empresa.nombreEmpresa,empresa.Cargo,empresa.TipodeIndustria,empresa.tamanodeEmpresa,empresa.Telefono,empresa.Correo,empresa.reto1,empresa.reto2,empresa.Dimension11,empresa.Dimension12,empresa.Dimension21,empresa.Dimension22,empresa.Dimension31,empresa.Dimension32,empresa.Dimension33,empresa.Dimension34,empresa.Dimension35,empresa.Dimension36,empresa.Dimension37,empresa.Dimension38,empresa.NivelIngresos,empresa.CostoDirectoComoPorcentaje,empresa.CostoDirecto,empresa.valorInventario])
        sheet = excel.pe.sheet.Sheet(empresas)
        return excel.make_response(sheet,file_type='csv',file_name='empresas')

admin.site.register(Empresa,EmpresaAdmin)
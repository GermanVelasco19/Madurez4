from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('Segunda/',views.segunda, name='Segunda'),
    path('Tercera/', views.tercera, name='Tercera'),
    path('Cuarta/', views.Cuarta, name='Cuarta'),
    path('Quinta/', views.Quinta, name='Quinta'),
    path('Sexta/', views.Sexta, name='Sexta'),
    path('Septima/', views.Septima, name='Septima'),
    path('Octava/', views.octava, name='Octava'),
    path('Novena/', views.Novena, name='Novena'),
    path('Decima/', views.Decima, name='Decima'),
    path('Onceava/', views.Onceava, name='Onceava'),
    path('Doceava/', views.Doceava, name='Doceava'),
    path('Treceava/', views.Treceava, name='Treceava'),  
    path('Catorce/', views.Catorce, name='Catorce'),
    #path('Resultados/', views.Resultados, name='Resultados'),
    path('Resultados/<str:NombreCompleto>/<str:nombreEmpresa>/<str:Cargo>/<str:TipodeIndustria>/<str:tamañodeEmpresa>/<str:Telefono>/<str:Correo>/<str:reto1>/<str:reto2>/<str:Dimension11>/<str:Dimension12>/<str:Dimension21>/<str:Dimension22>/<str:Dimension31>/<str:Dimension32>/<str:Dimension33>/<str:Dimension34>/<str:Dimension35>/<str:Dimension36>/<str:Dimension37>/<str:Dimension38>/<str:NivelIngresos>/<str:CostoDirectoComoPorcentaje>/<str:CostoDirecto>/<str:valorInventario>/', views.Resultados, name='Resultados'),
    path('Empresas/', views.EmpresasView.as_view(), name='Empresas'),
]




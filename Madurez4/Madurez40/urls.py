from django.urls import path
from . import views

urlpatterns = [
    path('Inicio/', views.inicio, name='Inicio'),
    path('Segunda/',views.segunda, name='Segunda'),
    path('Tercera/', views.tercera, name='Tercera'),
    path('Cuarta/', views.Cuarta, name='Cuarta'),
    path('Quinta/', views.Quinta, name='Quinta'),
    path('Sexta/', views.Sexta, name='Sexta'),
    path('Septima/', views.Septima, name='Septima'),
    path('Novena/', views.Novena, name='Novena'),
    path('Onceava/', views.Onceava, name='Onceava'),
    path('Treceava/', views.Treceava, name='Treceava'),    
]




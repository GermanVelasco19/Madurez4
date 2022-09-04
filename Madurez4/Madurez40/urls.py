from django.urls import path
from . import views

urlpatterns = [
    path('Inicio/', views.inicio, name='Inicio'),
    path('Tercera/', views.tercera, name='Tercera'),
    path('Quinta/', views.Quinta, name='Quinta'),
    path('Septima/', views.Septima, name='Septima'),
]




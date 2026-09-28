from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_instalaciones, name='lista_instalaciones'),
    path('agregar/', views.crear_instalacion, name='crear_instalacion'),
    path('editar/<int:pk>/', views.editar_instalacion, name='editar_instalacion'),
    path('eliminar/<int:pk>/', views.eliminar_instalacion, name='eliminar_instalacion'),
]
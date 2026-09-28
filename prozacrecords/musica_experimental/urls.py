from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_albumes, name='lista_albumes'),
    path('agregar/', views.crear_album, name='crear_album'),
    path('editar/<int:pk>/', views.editar_album, name='editar_album'),
    path('eliminar/<int:pk>/', views.eliminar_album, name='eliminar_album'),
]

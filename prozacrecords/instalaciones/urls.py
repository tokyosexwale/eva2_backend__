from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_instalaciones, name='lista_instalaciones'),
]
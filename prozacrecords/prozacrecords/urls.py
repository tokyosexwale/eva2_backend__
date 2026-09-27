from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('musica/', include('musica_experimental.urls')),
    path('instalaciones/', include('instalaciones.urls')),
]
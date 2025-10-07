from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name ='inicio'),
    path('nosotros', views.nosotros, name = 'nosotros'),
    path('vet/', views.listado, name='vet'),
    path('vet/crear', views.crear, name='crear'),
    path('vet/eliminar/<int:mascota_id>/', views.eliminar, name='eliminar')
    
]

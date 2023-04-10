from django.urls import path
from Aplicacion.views import inicio


urlpatterns = [ 
    path('', inicio, name = 'inicio'),
]
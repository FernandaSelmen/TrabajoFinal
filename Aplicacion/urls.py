from django.urls import path
from Aplicacion.views import inicio, exit, publicaciones, TextoListView, TextoDeleteViews, TextoCreateView, TextoDetailViews, TextoUpdateView, TextosListView

urlpatterns = [ 
    path('', inicio, name = 'inicio'),
    path('logout/', exit, name = 'exit'),
    path('publicaciones/', publicaciones, name = 'publicaciones'),
    path('mostrar_texto/',TextosListView.as_view(), name = 'mostrar_texto'),
    path('mostrar_view/',TextoListView.as_view(), name = 'mostrar_view'),
    path('borrar/<pk>', TextoDeleteViews.as_view(), name = 'eliminar_view'),
    path('agregar/', TextoCreateView.as_view(), name = 'agregar_view'),
    path('<pk>/', TextoDetailViews.as_view(), name = 'detalle_view'),
    path('editar/<pk>/', TextoUpdateView.as_view(), name = 'editar_view'),
]


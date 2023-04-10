from django.shortcuts import render
from Aplicacion.models import Texto
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

def inicio(request):
    return render(request, 'Aplicacion/index.html')

def publicaciones(request):
    return render(request, 'Aplicacion/publicaciones.html')



class TextoListView(ListView):
    model = Texto
    template_name = 'Aplicacion/mostrar_view.html'
   
class TextoDetailViews(DetailView):
    model = Texto
    template_name = 'Aplicacion/texto_detalle_view.html'

class TextoDeleteViews(DeleteView):
    model = Texto
    template_name = 'Aplicacion/texto_confirm_view.html'
    success_url = '/Aplicacion/mostrar_view/'


class TextoCreateView(CreateView):
    model = Texto
    template_name = 'Aplicacion/texto_form_view.html'
    success_url = '/Aplicacion/mostrar_view/'
    fields = ['titulo', 'subtitulo', 'contenido']

class TextoUpdateView(UpdateView):
    model = Texto
    template_name = 'Aplicacion/texto_form_view.html'
    success_url = '/Aplicacion/mostrar_view/'
    fields = ['titulo', 'subtitulo', 'contenido']

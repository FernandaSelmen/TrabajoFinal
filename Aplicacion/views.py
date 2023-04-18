from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from Aplicacion.models import Texto

# Create your views here.

def inicio(request):
    return render(request, 'Aplicacion/index.html')

def exit(request):
    logout(request)
    return redirect('inicio')

@login_required
def publicaciones(request):
    return render(request, 'Aplicacion/publicaciones.html')


def register(request):

    data = {'form': CustomUserCreationForm()}
        
    if request.method == "POST":

        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()

            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            return redirect('inicio')

    return render(request, 'registration/register.html', data)


class TextosListView(ListView):
    model = Texto
    template_name = 'Aplicacion/mostrar_texto.html'
    def get(self, request, *args, **kwargs): 
        return super().get(request, *args, **kwargs)


class TextoListView(ListView):
    model = Texto
    template_name = 'Aplicacion/mostrar_view.html'
   
class TextoDetailViews(DetailView):
    model = Texto
    template_name = 'Aplicacion/texto_detalle_view.html'

class TextoDeleteViews(DeleteView):
    model = Texto
    template_name = 'Aplicacion/texto_confirm_view.html'
    success_url = '/mostrar_view/'


class TextoCreateView(CreateView):
    model = Texto
    template_name = 'Aplicacion/texto_form_view.html'
    success_url = '/mostrar_view/'
    fields = ['titulo', 'subtitulo', 'contenido', 'imagen', 'dia']

class TextoUpdateView(UpdateView):
    model = Texto
    template_name = 'Aplicacion/texto_form_view.html'
    success_url = '/mostrar_view/'
    fields = ['titulo', 'subtitulo', 'contenido', 'imagen', 'dia']




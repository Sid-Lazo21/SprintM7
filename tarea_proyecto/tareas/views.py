from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import DetailView, UpdateView, ListView
from .models import Tarea
from .forms import TareaForm

class CrearTareaView(View):
    def get(self, request):
        form = TareaForm()
        return render(request, 'tareas/crear_tarea.html', {'form': form})

    def post(self, request):
        form = TareaForm(request.POST)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.asignada_a = request.user
            tarea.save()
            return redirect('lista_tareas')
        return render(request, 'tareas/crear_tarea.html', {'form': form})

class VerTareaView(DetailView):
    model = Tarea
    template_name = 'tareas/ver_tarea.html'
    context_object_name = 'tarea'

class EditarTareaView(UpdateView):
    model = Tarea
    form_class = TareaForm
    template_name = 'tareas/editar_tarea.html'
    context_object_name = 'tarea'

class ListarTareasView(ListView):
    model = Tarea
    template_name = 'tareas/listar_tarea.html'
    context_object_name = 'tareas'

def index(request):
    return render(request, 'tareas/index.html')









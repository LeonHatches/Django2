from django.shortcuts import get_object_or_404, redirect, render
from .models import Persona
from .forms import PersonaForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
def personaTestView(request):
    obj = Persona.objects.get(id = 1)
    context = {
        'objeto': obj
    }

    return render(request, "personas/descripcion.html", context)

def searchForHelp (request):
    return render(request, 'personas/search.html', {})

def personaCreateView(request):
    initialValues = {
        'nombres': 'Sin Nombre'
    }
    form = PersonaForm(request.POST or None, initial = initialValues)
    if form.is_valid():
        form.save()
        form = PersonaForm()

    context = {
        'form': form
    }

    return render(request, 'personas/personasCreate.html', context)

class personaListView(ListView):
    model = Persona
    queryset = Persona.objects.filter(edad__lte='40')

class personaDeleteView (DeleteView):
    model = Persona
    success_url = reverse_lazy('persona:persona-list')

def personasShowObject (request, myID):
    obj = get_object_or_404(Persona, id=myID)
    context = {
        'objeto': obj,
    }
    return render(request, 'personas/descripcion.html', context)

class personaDetailView (DetailView):
    model = Persona

class personaCreateView (CreateView):
    model = Persona
    fields = [
        'nombres',
        'apellidos',
        'edad',
        'menor'
    ]

class personaUpdateView (UpdateView):
    model = Persona
    fields = [
        'nombres',
        'apellidos',
        'edad',
        'menor'
    ]
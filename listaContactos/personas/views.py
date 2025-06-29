from django.shortcuts import get_object_or_404, render
from .models import Persona
from .forms import PersonaForm

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

def personaListView (request):
    queryset = Persona.objects.all

    context = {
        'objectList': queryset,
    }
    return render(request, 'personas/personasLista.html', context)

def personaDeleteView(request, myID):
    obj = get_object_or_404(Persona, id=myID)
    if request.method == 'POST':
        print("Se borro")
        obj.delete()
    
    context = {
        'objecto': obj,
    }

    return render(request, 'personas/personasBorrar.html', context)
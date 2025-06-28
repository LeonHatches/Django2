from django.shortcuts import render
from .models import Persona
from .forms import RawPersonaForm

# Create your views here.
def personaTestView(request):
    obj = Persona.objects.get(id = 1)
    context = {
        'objeto': obj
    }

    return render(request, "personas/descripcion.html", context)

def searchForHelp (request):
    return render(request, 'personas/search.html', {})

def personaAnotherCreateView(request):
    form = RawPersonaForm()
    if request.method == "POST":
        form = RawPersonaForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Persona.objects.create(**form.cleaned_data)
        else:
            print(form.errors)
    
    context = {
        'form': form,
    }
    return render(request, 'personas/personasCreate.html', context)
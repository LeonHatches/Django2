from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myHomeView(request, *args, **kwargs):
    
    myContext = {
        'myText': 'Esto es sobre nosotros',
        'myNumber': 123,
    }

    return render (request, "home.html", myContext)

def anotherView(request):
    return HttpResponse('<h1>Esta es la otra página :)</h1>')

def hiddenView(request):
    return HttpResponse('<h1>Esta página esta oculta...</h1>')
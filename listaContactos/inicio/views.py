from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myHomeView(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    items=['Primero','Segundo','Tercero']
    return render (request, "home.html", {'items': items})

def anotherView(request):
    return HttpResponse('<h1>Esta es la otra página :)</h1>')

def hiddenView(request):
    return HttpResponse('<h1>Esta página esta oculta...</h1>')
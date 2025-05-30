from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myHomeView(*args, **kwargs):
    return HttpResponse('<h1>Hola Mundito desde Django</h1>')

def anotherView(request):
    return HttpResponse('<h1>Esta es la otra página :)</h1>')

def hiddenView(request):
    return HttpResponse('<h1>Esta página esta oculta...</h1>')
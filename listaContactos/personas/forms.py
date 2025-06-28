from django import forms

class RawPersonaForm (forms.Form):
    nombres   = forms.CharField()
    apellidos = forms.CharField()
    edad      = forms.IntegerField()
    menor     = forms.BooleanField()
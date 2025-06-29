from django import forms
from .models import Persona

class PersonaForm (forms.ModelForm):
    class Meta:
        model = Persona
        fields = [
            'nombres',
            'apellidos',
            'edad',
            'menor',
        ]
    
    def clean_nombres(self, *args, **kwargs):
        print('paso')
        name = self.cleaned_data.get('nombres')
        if name.istitle():
            return name
        else:
            raise forms.ValidationError('La primera letra en Mayúscula')
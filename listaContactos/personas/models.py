from django.db import models
from django.urls import reverse

# Create your models here.
class Persona (models.Model):
    nombres   = models.CharField()
    apellidos = models.CharField()
    edad      = models.IntegerField()
    menor     = models.BooleanField()

    def get_absolute_url (self):
        return reverse('personas:browsing', kwargs={'myID': self.id})

    def __str__(self):
        return self.nombres
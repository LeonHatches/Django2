from django.db import models

# Create your models here.
class Persona (models.Model):
    nombres   = models.CharField()
    apellidos = models.CharField()
    edad      = models.IntegerField()
    menor     = models.BooleanField()

    def get_absolute_url (self):
        return "/personas/"+str(self.id)+"/"

    def __str__(self):
        return self.nombres
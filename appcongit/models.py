from django.db import models

# Create your models here.
class Persona(models.Model):
    rut=models.TextField(max_length=10,primary_key=True)
    nombre=models.TextField(max_length=50)
    apellido=models.TextField(max_length=50)
    
    def __str__(self):
        return f"{self.rut}-{self.nombre} {self.apellido}"


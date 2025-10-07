from django.db import models

# Aqui esta el modelo base de lo que se solicita al usuario

class Mascota(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    motivo = models.CharField(max_length=200) 
    especie = models.CharField(max_length=50)

    
    
    

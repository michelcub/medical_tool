from django.db import models


import uuid
# Create your models here.
class Paciente(models.Model):
    id = models.AutoField(primary_key=True)
    key = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, null=False)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    fecha_registro = models.DateField(auto_now_add=True)
    photo = models.URLField(max_length=200, default="https://www.pngitem.com/pimgs/m/146-1468479_my-profile-icon-blank-profile-picture-circle-hd.png")
    LPD = models.URLField(max_length=200)
    
    
class Historial(models.Model):
    id = models.AutoField(primary_key=True)
    key = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, null=False)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    
    
class Episodio(models.Model):
    id = models.AutoField(primary_key=True)
    key = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, null=False)
    historial = models.ForeignKey(Historial, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    diagnostico = models.TextField()
    alergias = models.TextField()
    seguimiento = models.TextField()
    recomendacion = models.TextField()
    
    
class Receta(models.Model):
    id = models.AutoField(primary_key=True)
    key = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, null=False)
    episodio = models.ForeignKey(Episodio, on_delete=models.CASCADE)
    medicamento = models.CharField(max_length=50)
    dosis = models.CharField(max_length=50)
    frecuencia = models.CharField(max_length=50)
    duracion = models.CharField(max_length=50)
    observaciones = models.TextField()
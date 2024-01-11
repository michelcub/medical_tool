from django.db import models


import uuid
# Create your models here.
class Paciente(models.Model):
    id = models.AutoField(primary_key=True)
    key = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, null=False)
    comentario = models.CharField(max_length=400, default='n/a')
    nombre = models.CharField(max_length=50, null=False, default='n/a')
    apellidos = models.CharField(max_length=100, default='n/a')
    fecha_nacimiento = models.CharField(max_length=100, default='n/a')
    tipo_documento = models.CharField(max_length=100, default='n/a')
    documento_identidad = models.CharField(max_length=100, default='n/a')
    sexo = models.CharField(max_length=100, default='n/a')
    telefono = models.CharField(max_length=100, default='n/a')
    telefono_adicional = models.CharField(max_length=100, default='n/a')
    email = models.CharField(max_length=100, default='n/a')
    
    calle = models.CharField(max_length=100, default='n/a')
    numero = models.CharField(max_length=100, default='n/a')
    puerta = models.CharField(max_length=100, default='n/a')
    pais = models.CharField(max_length=100, default='n/a')
    ciudad = models.CharField(max_length=100, default='n/a')
    cp = models.CharField(max_length=100, default='n/a')
    
    aseguradora = models.CharField(max_length=100, default='n/a')
    numero_seguro = models.CharField(max_length=100, default='n/a')
    otros_datos = models.TextField(default='n/a')
    
    fecha_registro = models.DateField(auto_now_add=True)
    photo = models.URLField(max_length=200, default="https://www.pngitem.com/pimgs/m/146-1468479_my-profile-icon-blank-profile-picture-circle-hd.png")
    LPD = models.URLField(max_length=200, default='n/a')
    
    
    
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
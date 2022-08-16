from django.db import models

# Create your models here.

class Registro(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    usuario = models.CharField(max_length=20, unique=True)
    correo_Electronico = models.CharField(max_length=100, unique=True)
    contraseña = models.CharField(max_length=20, unique=True)
    repetir_Contraseña = models.CharField(max_length=20, unique=True)
    
class Destino(models.Model):
    destinos =  models.CharField(max_length=50)
    terminal = models.CharField(max_length=50)
    fecha_ida = models.CharField(max_length=50)
    fecha_vuelta = models.CharField(max_length=50, blank=True)
    
class Opinion(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo_Electronico = models.CharField(max_length=100)
    opinion = models.CharField(max_length=5000)
    
class Recuperacion(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo_Electronico = models.CharField(max_length=100)
    
class Datos_Tarjeta(models.Model):
    numero_Tarjeta = models.CharField(max_length=19)
    nombre_Tarjeta = models.CharField(max_length=50)
    mes_Expiracion = models.IntegerField()
    anio_Expiracion = models.IntegerField()
    CCV = models.IntegerField()
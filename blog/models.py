from django.db import models
from django.utils import timezone

#modelo proyecto
class Proyecto(models.Model):
    nombre = models.CharField('Nombre proyecto',max_length=150)
    empresa = models.CharField('Nombre de la Institucion o Empresa',max_length=150)
    tipo_proyecto= models.CharField('Proyecto: INTERNO o EXTERNO',max_length=1)
    descripcion = models.CharField('Descripcion del proyecto',max_length=255)
    estado = models.CharField('Proyecto: Asignado o NO Asignado',max_length=10)
    matricula = models.CharField('Matricula Asignada',max_length=10)
    created_date = models.DateTimeField(
            default=timezone.now)
# modelo carrera
class Carrera(models.Model):
    nombre = models.CharField('Nombre Carrera',max_length=150)    
    created_date = models.DateTimeField(
            default=timezone.now)
# modelo EMPRESA
class Empresa(models.Model):
    nombre = models.CharField('Nombre de la Empresa',max_length=150)
    titularempresa = models.CharField('Titular de la Empresa',max_length=150)
    giro = models.CharField('Giro de la Empresa',max_length=100)
    titularproyecto = models.CharField('Titular del Proyecto',max_length=150)
    direccion = models.CharField('Calle y Numero',max_length=255)
    colonia = models.CharField('Colonia',max_length=255)
    codigo_postal =models.CharField('Codigo Postal',max_length=50)
    rfc = models.CharField('RFC',max_length=100)
    telefono = models.CharField('Telefono',max_length=50)
    email = models.CharField('Email',max_length=100)
    social = models.CharField('Redes Sociales',max_length=255)
    created_date = models.DateTimeField(
            default=timezone.now)
   
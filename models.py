from django.db import models

class Animal(models.Model):
    id_animal = models.AutoField(primary_key=True, db_column='ID_Animal')  # Define la clave primaria
    nombre = models.CharField(max_length=50)
    especie = models.CharField(max_length=50)
    raza = models.CharField(max_length=50, null=True, blank=True)
    edad = models.PositiveIntegerField()
    sexo = models.CharField(max_length=10)
    estado_salud = models.CharField(max_length=100)
    estado_disponibilidad = models.CharField(max_length=20, default='Disponible')
    fecha_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Animales'  # Nombre exacto de la tabla en la base de datos


# Create your models here.
from django.db import models

class Adoptante(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

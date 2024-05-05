from django.db import models

# Create your models here.

# tabla Autores
class Autores(models.Model):
    # atributos
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=50)
    website = models.EmailField()

# tabla Temática
class Tematicas(models.Model):
    # atributos
    Titulo = models.CharField(max_length=30)
    Codigo = models.CharField(max_length=3)


# tabla Artículos
class Articulos(models.Model):
    # atributos
    titulo = models.CharField(max_length=100)
    dia_publicacion = models.DateField()
    
    # relaciones
    autores = models.ManyToManyField(Autores)
    tematica = models.ForeignKey(Tematicas, on_delete=models.CASCADE)


from django.db import models

class Item(models.Model):
    titulo = models.CharField(max_length=150)
    categoria = models.CharField(max_length=50)
    descripcion = models.TextField()
    anio = models.IntegerField()

    def __str__(self):
        return self.titulo
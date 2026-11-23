from django.db import models
from catalogo.models import Item

class Resena(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='resenas')
    autor = models.CharField(max_length=100)
    puntuacion = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comentario = models.TextField()
    creado_en =  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.autor} - {self.item.titulo} ({self.puntuacion}/5)"
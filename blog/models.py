from django.db import models


class Articulo(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
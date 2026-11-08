from django.db import models
from django.utils.text import slugify


class Articulo(models.Model):
    titulo = models.CharField(
        max_length=200,
        verbose_name="Título"
    )
    slug = models.SlugField(
        max_length=200,
        unique=True,
        blank=True,
        verbose_name="Slug (URL)"
    )
    autor = models.CharField(
        max_length=100,
        default="Anónimo",
        verbose_name="Autor"
    )
    resumen = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="Resumen corto"
    )
    contenido = models.TextField(
        verbose_name="Contenido"
    )
    imagen = models.ImageField(
        upload_to='articulos/',
        blank=True,
        null=True,
        verbose_name="Imagen de portada"
    )
    publicado = models.BooleanField(
        default=True,
        verbose_name="¿Publicado?"
    )
    creado = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha de creación"
    )
    actualizado = models.DateTimeField(
        auto_now=True,
        verbose_name="Última actualización"
    )

    class Meta:
        ordering = ['-creado']
        verbose_name = "Artículo"
        verbose_name_plural = "Artículos"

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        # Genera el slug automáticamente a partir del título
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)
from django.db import models
from django.conf import settings
from django.urls import reverse


class Post(models.Model):
    titulo = models.CharField(max_length=255)
    subtitulo = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    resumen = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    cuerpo = models.TextField()
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    categorias = models.ManyToManyField('Categoria')
    destacado = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('blogs:post',kwargs={'slug':self.slug})
    
    def __str__(self):
        return self.titulo

class Categoria(models.Model):
    titulo = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.titulo
    
    def get_absolute_url(self):
        return reverse('blogs:categoria',kwargs={'slug':self.slug})
from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils import timezone


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
    imagen = models.ImageField(upload_to='media/imagenes/',blank=True, null=True)
    fecha_publicacion = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('blogs:post',kwargs={'slug':self.slug})
    
    class meta:
        ordering = ['-fecha_publicacion']
    
    def __str__(self):
        return self.titulo

class Categoria(models.Model):
    titulo = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.titulo
    
    def get_absolute_url(self):
        return reverse('blogs:categoria',kwargs={'slug':self.slug})
    
class Comentario(models.Model):
    contenido = models.TextField(max_length=1500, help_text='Ingrese un comentario')
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,null=True)
    fecha_comentario= models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['-fecha_comentario']
    
    def __str__(self):
        len_title =15
        if len(self.contenido)>len_title:
            return self.contenido[:len_title] + '...'
        return self.contenido
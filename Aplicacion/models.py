from django.db import models

# Create your models here.

class Texto(models.Model):
    titulo = models.CharField(max_length=40)
    subtitulo = models.CharField(max_length=30)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='media/texto', null= True)
    dia = models.DateField(("dia"), auto_now=False, auto_now_add=False)
    def __str__(self):
        return f'{self.id} Titulo: {self.titulo} Subtitulo: {self. subtitulo}'

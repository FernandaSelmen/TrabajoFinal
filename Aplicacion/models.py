from django.db import models

# Create your models here.

class Texto(models.Model):
    titulo = models.CharField(max_length=40)
    subtitulo = models.CharField(max_length=30)
    contenido = models.TextField()
from django.db import models

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=20)
    contenido = models.CharField(max_length=500)
    fecha = models.DateField(auto_now=True)

    def __str__(self):
        return self.titulo
    
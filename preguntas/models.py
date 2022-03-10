from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Pregunta(models.Model):
    pregunta = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return self.pregunta

class Respuesta(models.Model):
    respuesta = models.TextField()
    owner = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return self.respuesta

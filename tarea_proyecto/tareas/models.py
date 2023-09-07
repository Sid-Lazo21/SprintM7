from django.db import models

class Prioridad(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        app_label = 'tareas'

    def __str__(self):
        return self.nombre

class Tarea(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    asignada_a = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    prioridad = models.ForeignKey(Prioridad, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
    




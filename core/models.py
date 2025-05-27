from django.db import models
from django.contrib.auth.models import User

class Plato(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.nombre

class Orden(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    platos = models.ManyToManyField(Plato)
    fecha = models.DateTimeField(auto_now_add=True)
    pagada = models.BooleanField(default=False)

    def __str__(self):
        return f"Orden {self.id} - {self.usuario.username}"

class Pago(models.Model):
    orden = models.OneToOneField(Orden, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=8, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pago de la orden {self.orden.id}"
from django.db import models

# Create your models here.


class Edificio(models.Model):
    class Meta:
        ordering = ["nombre"]
        verbose_name_plural = "Los Edificios"

    opciones_tipo = (
        ('1', 'Residencial'),
        ('2', 'Comercial'),
    )

    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30, choices=opciones_tipo)

    def __str__(self):
        return "%s - %s - %s - %s" % (self.nombre, self.direccion, self.ciudad,
                                      self.tipo)

    def obtener_cantidad_cuartos(self):
        valor = [t.num_cuartos for i in self.departamentos.all()]
        valor = sum(valor)
        return valor

    def obtener_costo_departamento(self):
        valor = [t.costo for i in self.departamentos.all()]
        valor = sum(valor)
        return valor


class Departamento(models.Model):
    class Meta:
        ordering = ["nombreProp"]
        verbose_name_plural = "Los Departamentos"

    nombreProp = models.CharField(max_length=150)
    costo = models.FloatField()
    numCuartos = models.IntegerField()
    edificio = models.ForeignKey(Edificio, related_name="edificio",
                                 on_delete=models.CASCADE)

    def __str__(self):
        return "%s - %.2f - %d - %s" % (self.nombreProp,
                                        self.costo, self.numCuartos, self.edificio)

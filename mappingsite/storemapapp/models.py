from __future__ import unicode_literals

from django.db import models


class Ruc(models.Model):
    Nombre = models.CharField(max_length=100, blank=True, null=True)
    Provincia = models.CharField(max_length=100, blank=True, null=True)
    Condicion = models.CharField(max_length=100, blank=True, null=True)
    Ruc = models.CharField(max_length=100, blank=True, null=True)
    Departamento = models.CharField(max_length=100, blank=True, null=True)
    Domicilio = models.CharField(max_length=100, blank=True, null=True)
    Distrito = models.CharField(max_length=100, blank=True, null=True)
    Estado = models.CharField(max_length=100, blank=True, null=True)
    Ubigeo = models.CharField(max_length=100, blank=True, null=True)

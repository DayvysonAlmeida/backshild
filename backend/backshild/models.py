from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    setor = models.CharField(max_length=100, blank=True, null=True)  # Ex.: TI, Administrativo



class Setor(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class TipoEquipamento(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Equipamento(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.ForeignKey(TipoEquipamento, on_delete=models.CASCADE)
    marca = models.CharField(max_length=100, blank=True, null=True)
    modelo = models.CharField(max_length=100, blank=True, null=True)
    service_tag = models.CharField(max_length=50, blank=True, null=True)
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)  # True: Disponível | False: Empréstimo

    def __str__(self):
        return self.nome

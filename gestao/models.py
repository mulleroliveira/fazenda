from django.db import models

class Animal(models.Model):
      nome = models.CharField(max_length=20)
      sexo = models.CharField(max_length=1, choices=[('M','Macho'),('F','Fêmea')])
      raca = models.CharField(max_length=20, verbose_name='Raça')
      cientifico = models.CharField(max_length=20, verbose_name='Nome Científico')
      peso = models.DecimalField(max_digits=6, decimal_places=2)
      tamanho = models.DecimalField(max_digits=5,decimal_places=2)
      expectativa = models.IntegerField(verbose_name='Expectativa de Vida')
      objetivo = models.CharField(max_length=10, choices=[('Abate','Abate'),('Reprodutor','Reprodutor')])
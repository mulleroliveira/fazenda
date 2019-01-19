from django.db import models

class Animal(models.Model):

      especialidade_choices = (
            ('Abate', 'Abate'),
            ('Reprodutor', 'Reprodutor')
      )

      nome = models.CharField(max_length=20)
      cientifico = models.CharField(max_length=20, verbose_name='Nome Científico')
      expectativa = models.CharField(max_length=10, verbose_name='Expectativa de Vida')
      periodo = models.CharField(max_length=10, verbose_name='Periodo de Gestação')
      peso = models.DecimalField(max_digits=6, decimal_places=2)
      velocidade = models.IntegerField()
      codigo = models.CharField(max_length=11, verbose_name='Código de Identificação')
      raca = models.CharField(max_length=20, verbose_name='Raça')
      objetivo = models.CharField(max_length=10, choices=especialidade_choices)
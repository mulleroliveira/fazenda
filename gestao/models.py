from django.db import models

class Animal(models.Model):
      nome = models.CharField(max_length=20)
      sexo = models.CharField(max_length=1, choices=[('M','Macho'),('F','Fêmea')])
      raca = models.CharField(max_length=20, verbose_name='Raça')
      cientifico = models.CharField(max_length=20, verbose_name='Nome Científico')
      peso = models.DecimalField(max_digits=6, decimal_places=2)
      tamanho = models.DecimalField(max_digits=5,decimal_places=2)
      expectativa = models.IntegerField(verbose_name='Expectativa de Vida')
      tipo_criacao = models.CharField(max_length=10, choices=[('Abate','Abate'),('Reprodutor','Reprodutor')])

class Fazendeiro(models.Model):

      choices_estado = (
            ('AC','Acre'),
            ('ALA','lagoas'),
            ('AP','Amapá'),
            ('AMA','mazonas'),
            ('BA','Bahia'),
            ('CE','Ceará'),
            ('DF','Distrito Federal'),
            ('ES','Espírito Santo'),
            ('GO','Goiás'),
            ('MA','Maranhão'),
            ('MT','Mato Grosso'),
            ('MS','Mato Grosso do Sul'),
            ('MG','Minas Gerais'),
            ('PA','Pará'),
            ('PB','Paraíba'),
            ('PR','Paraná'),
            ('PE','Pernambuco'),
            ('PI','Piauí'),
            ('RR','Roraima'),
            ('RO','Rondônia'),
            ('RJ','Rio de Janeiro'),
            ('RN','Rio Grande do Norte'),
            ('RS','Rio Grande do Sul'),
            ('SC','Santa Catarina'),
            ('SP','São Paulo'),
            ('SE','Sergipe'),
            ('TO','Tocantins'),
      )

      sexo_choices = (
            ('M','Masculino'),
            ('F','Feminino')
      )

      nome = models.CharField(max_length=20)
      sexo = models.CharField(max_length=1, choices=sexo_choices)
      data_nasc = models.DateField()
      cpf = models.CharField(max_length=11)
      rg = models.CharField(max_length=9)
      funcao = models.CharField(max_length=20)
      peso = models.DecimalField(max_digits=5, decimal_places=2)
      altura = models.DecimalField(max_digits=3, decimal_places=2)
      cidade = models.CharField(max_length=20)
      estado = models.CharField(max_length=2, choices=choices_estado)
      salario = models.DecimalField(max_digits=6, decimal_places=2)
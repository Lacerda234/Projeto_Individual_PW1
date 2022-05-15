from django.db import models

SEXO_CHOICES=[
    ('m', 'Masculino'),
    ('f', 'Feminino')
]

TIPO_CHOICES=[
    ('g', 'Gato'),
    ('c', 'Cachorro')
]

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=30)
    cpf = models.IntegerField(blank=True, null=True)
    telefone = models.IntegerField(blank=True, null=True)
    idade = models.IntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    data_nascimento = models.DateField(blank=True, null=True)
    profissão = models.CharField(max_length=30)

    def __str__(self):
        return self.nome


class Animal(models.Model):
    nome = models.CharField(max_length=20)
    raça = models.CharField(max_length=15)
    data_nascimento = models.DateField(blank=True, null=True)
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    observações = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome
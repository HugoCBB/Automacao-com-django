from django.db import models

# Create your models here.

class Cliente(models.Model):
    ESTADO_DO_CLIENTE = [
        ('Matriculado', 'Matriculado'),
        ('Não Matriculado', 'Não Matriculado'),
    ]
    data = models.DateField(auto_now_add=True)
    nome = models.CharField(max_length=30)
    numero = models.CharField(max_length=15, blank=False, null=False)
    matriculado = models.CharField(max_length=15, choices=ESTADO_DO_CLIENTE, default='Não Matriculado')


    def __str__(self):
        return self.nome
    

class Mensagem(models.Model):
    data = models.DateField(auto_now_add=True)
    mensagem = models.TextField(max_length=500)

    def __str__(self):
        return self.mensagem
    
    
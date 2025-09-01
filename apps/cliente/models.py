from django.db import models

# Create your models here.
class Cliente(models.Model):
    ESTADO_DO_CLIENTE = [
        ('Ativo', 'ativo'),
        ('Inativo', 'inativo'),
    ]
    data = models.DateField(auto_now_add=True)
    nome = models.CharField(max_length=30,  blank=True, null=True)
    numero = models.CharField(max_length=15, blank=False, null=False)
    status = models.CharField(max_length=15, choices=ESTADO_DO_CLIENTE, default='Ativo')
    
    def __str__(self):
        return self.nome
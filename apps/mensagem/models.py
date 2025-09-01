from django.db import models

# Create your models here.
class Mensagem(models.Model):
    data = models.DateField(auto_now_add=True)
    mensagem = models.TextField(max_length=500)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.mensagem
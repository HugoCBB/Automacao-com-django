from django.forms import ModelForm
from . models import Mensagem, Cliente

class MensagemForm(ModelForm):
    class Meta:
        model = Mensagem
        fields = '__all__'

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
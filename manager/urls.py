from django.urls import path
from .views import home, EnviarMensagens, AdicionarMensagem, AdicionarCliente, MensagensSalvas, ClientesSalvos

urlpatterns = [
    path('',home,name='home'),
    path('enviar-mensagem/<int:mensagem_id>', EnviarMensagens, name='enviar-mensagem'),
    path('adicionar-mensagem', AdicionarMensagem, name='adicionar-mensagens'),
    path('adicionar-cliente', AdicionarCliente, name='adicionar-cliente'),
    path('mensagens-salvas', MensagensSalvas, name='mensagens-salvas'),
    path('clientes-salvos', ClientesSalvos, name='clientes-salvos'),

]

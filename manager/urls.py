from django.urls import path
from .views import home, EnviarMensagens, AdicionarMensagem, AdicionarCliente, MensagensSalvas, ClientesSalvos, EditarCliente, EditarMensagem, DeletarCliente, DeletarMensagem

urlpatterns = [
    path('',home,name='home'),
    path('enviar-mensagem/<int:mensagem_id>', EnviarMensagens, name='enviar-mensagem'),
    path('adicionar-mensagem', AdicionarMensagem, name='adicionar-mensagens'),
    path('adicionar-cliente', AdicionarCliente, name='adicionar-cliente'),
    path('mensagens-salvas', MensagensSalvas, name='mensagens-salvas'),
    path('clientes-salvos', ClientesSalvos, name='clientes-salvos'),
    path('editar-cliente/<int:cliente_id>', EditarCliente, name="editar-cliente"),
    path('editar-mensagem/<int:mensagem_id>', EditarMensagem, name="editar-mensagem"),
    path('deletar-cliente/<int:cliente_id>',DeletarCliente, name='deletar-cliente'),
    path('deletar-mensagem/<int:mensagem_id>',DeletarMensagem, name='deletar-mensagem'),

]

from django.urls import path
from .views import EnviarMensagens, AdicionarMensagem, MensagensSalvas, DeletarMensagem, home, EditarMensagem


urlpatterns = [
    path('home', home, name='home'),
    path('enviar-mensagem/<int:mensagem_id>', EnviarMensagens, name='enviar-mensagem'),
    path('adicionar-mensagem', AdicionarMensagem, name='adicionar-mensagens'),
    path('mensagens-salvas', MensagensSalvas, name='mensagens-salvas'),
    path('deletar-mensagem/<int:mensagem_id>',DeletarMensagem, name='deletar-mensagem'),
    path('editar-mensagem/<int:mensagem_id>', EditarMensagem, name='editar-mensagem')

]
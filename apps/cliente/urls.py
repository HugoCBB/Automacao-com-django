from django.urls import path
from .views import  AdicionarCliente, ClientesSalvos, DeletarCliente, EditarCliente


urlpatterns = [
    path('adicionar-cliente', AdicionarCliente, name='adicionar-cliente'),
    path('clientes-salvos', ClientesSalvos, name='clientes-salvos'),
    path('deletar-cliente/<int:cliente_id>',DeletarCliente, name='deletar-cliente'),
    path('editar-cliente/<int:cliente_id>',EditarCliente, name='editar-cliente'),

]

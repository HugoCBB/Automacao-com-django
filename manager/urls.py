from django.urls import path
from .views import home, EnviarMensagens

urlpatterns = [
    path('',home,name='home'),
    path('mensagem', EnviarMensagens, name='mensagens')

]

from django.shortcuts import render, HttpResponse
from django.shortcuts import get_object_or_404
from . models import Cliente, Mensagem
from . selenium_service import SUN_BOT



# Create your views here.
def home(request):
    clientes = Cliente.objects.all()
    return render(request, 'manager/home.html',{'clientes':clientes})

def EnviarMensagens(request):
    clientes = Cliente.objects.filter(numero__isnull=False)
    mensagem = get_object_or_404(Mensagem, pk=1 )
    # mensagem = Mensagem.objects.filter(mensagem__isnull=False)
    try:
        resposta = SUN_BOT()
        resposta.AcessarSite()
        for cliente in clientes:
            resposta.EnviarMensagem(cliente.numero, mensagem.mensagem)
    except Exception as e:
        print(e)
    finally:
        resposta.EncerrarPrograma()
    return HttpResponse('Mensagens enviadas')
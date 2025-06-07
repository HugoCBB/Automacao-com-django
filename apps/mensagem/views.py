from django.shortcuts import render, HttpResponse, redirect
from django.shortcuts import get_object_or_404
from automation.selenium.bot_envio_mensagens import SUN_BOT

from apps.cliente.models import Cliente

from .models import Mensagem
from . forms import MensagemForm


def home(request):
    return render(request, 'home.html')


def MensagensSalvas(request):
    mensagem = Mensagem.objects.all()
    return render(request,'mensagem/mensagensSalvas.html',{'mensagem':mensagem})


# Criar nova mensagem
def AdicionarMensagem(request):
    form = MensagemForm(request.POST)
    
    if request.method == 'POST':
        form = MensagemForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('mensagens-salvas')

    return render(request, 'mensagem/mensagemForm.html',{'form':form})

def EnviarMensagens(request, mensagem_id):
    clientes = Cliente.objects.filter(status='Ativo')
    mensagem = get_object_or_404(Mensagem, pk=mensagem_id)

    try:
        
        resposta = SUN_BOT()
        resposta.AcessarSite()
        for cliente in clientes:
            resposta.EnviarMensagem(cliente.nome, cliente.numero, mensagem)
        mensagem.status = True
        mensagem.save()
        return HttpResponse('Mensagens enviadas com sucesso')
    except Exception as e:
        print(e)
        return HttpResponse('Erro ao enviar mensagem')
    finally:
        resposta.EncerrarPrograma()


def DeletarMensagem(request, mensagem_id):
    mensagem = Mensagem.objects.get(id=mensagem_id)
    mensagem.delete()
    return redirect('mensagens-salvas')


def EditarMensagem(request, mensagem_id):
    mensagem = Mensagem.objects.get(id=mensagem_id)
    form = MensagemForm(instance=mensagem)
    if request.method == 'POST':
        form = MensagemForm(request.POST, instance=mensagem)
        form.save()
        return redirect('mensagens-salvas')
    return render(request, 'mensagem/editarMensagem.html',{'form':form, 'mensagem_id':mensagem_id})

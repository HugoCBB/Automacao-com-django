from django.shortcuts import render, HttpResponse, redirect
from django.shortcuts import get_object_or_404
from .selenium.bot_envio_mensagens import SUN_BOT

from . models import Cliente, Mensagem
from . forms import MensagemForm, ClienteForm


# Create your views here.
def home(request):
    return render(request, 'manager/home.html')

def ClientesSalvos(request):
    clientes = Cliente.objects.all()
    return render(request, 'manager/clientes_salvos.html',{'clientes':clientes})

def MensagensSalvas(request):
    mensagem = Mensagem.objects.all()
    return render(request,'manager/mensagens_salvas.html',{'mensagem':mensagem})

# Cadastrar novo cliente
def AdicionarCliente(request):
    form = ClienteForm(request.POST)
    
    if request.method == 'POST':
        form = ClienteForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('adicionar-cliente')
    return render(request, 'manager/clienteform.html',{'form':form})

# Criar nova mensagem
def AdicionarMensagem(request):
    form = MensagemForm(request.POST)
    
    if request.method == 'POST':
        form = MensagemForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('mensagens-salvas')

    return render(request, 'manager/mensagemform.html',{'form':form})


# Enviar mensagem
def EnviarMensagens(request, mensagem_id):
    clientes = Cliente.objects.filter(matriculado='Não Matriculado')
    mensagem = get_object_or_404(Mensagem, pk=mensagem_id)

    try:
        resposta = SUN_BOT()
        resposta.AcessarSite()
        for cliente in clientes:
            resposta.EnviarMensagem(cliente.nome, cliente.numero, mensagem.mensagem)
        mensagem.status = True
        mensagem.save()
        return HttpResponse('Mensagens enviadas com sucesso')
    except Exception as e:
        print(e)
        return HttpResponse('Erro ao enviar mensagem')
    finally:
        resposta.EncerrarPrograma()


def EditarCliente(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    form = ClienteForm(instance=cliente)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        form.save()
        return redirect('clientes-salvos')
    return render(request, 'manager/editar_cliente.html',{'form':form, 'cliente_id':cliente_id})

def EditarMensagem(request, mensagem_id):
    mensagem = Mensagem.objects.get(id=mensagem_id)
    form = MensagemForm(instance=mensagem)
    if request.method == 'POST':
        form = MensagemForm(request.POST, instance=mensagem)
        form.save()
        return redirect('mensagens-salvas')
    return render(request, 'manager/editar_mensagem.html',{'form':form, 'mensagem_id':mensagem_id})


def DeletarCliente(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    cliente.delete()
    return redirect('clientes-salvos')

def DeletarMensagem(request, mensagem_id):
    mensagem = Mensagem.objects.get(id=mensagem_id)
    mensagem.delete()
    return redirect('mensagens-salvas')
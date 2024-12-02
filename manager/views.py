from django.shortcuts import render, HttpResponse, redirect
from django.shortcuts import get_object_or_404
from . selenium_service import SUN_BOT

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
            return redirect('home')
    return render(request, 'manager/clienteform.html',{'form':form})

# Criar nova mensagem
def AdicionarMensagem(request):
    form = MensagemForm(request.POST)
    
    if request.method == 'POST':
        form = MensagemForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'manager/mensagemform.html',{'form':form})


# Enviar mensagem
def EnviarMensagens(request, mensagem_id):
    clientes = Cliente.objects.filter(matriculado=False)
    mensagem = get_object_or_404(Mensagem, pk=mensagem_id)
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
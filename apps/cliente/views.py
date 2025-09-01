from django.shortcuts import render, HttpResponse, redirect
from django.shortcuts import get_object_or_404
from automation.selenium.bot_envio_mensagens import SUN_BOT

from . models import Cliente
from . forms import ClienteForm


def ClientesSalvos(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente/clientesSalvos.html',{'clientes':clientes})


# Cadastrar novo cliente
def AdicionarCliente(request):
    form = ClienteForm(request.POST)
    
    if request.method == 'POST':
        form = ClienteForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('adicionar-cliente')
    return render(request, 'cliente/clienteForm.html',{'form':form})


def DeletarCliente(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    cliente.delete()
    return redirect('clientes-salvos')


def EditarCliente(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    form = ClienteForm(instance=cliente)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        form.save()
        return redirect('clientes-salvos')
    return render(request, 'cliente/editarCliente.html',{'form':form, 'cliente_id':cliente_id})

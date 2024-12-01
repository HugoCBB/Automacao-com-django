from django.shortcuts import render, HttpResponse
from . models import Cliente, Mensagem

# Create your views here.
def home(request):
    return render(request,'manager/home.html')

def EnviarMensagens(request):
    clientes = Cliente.objects.filter(numero__isnull=False)
    for cliente in clientes:
        numero = cliente.numero

        print(f'Enviando mensagem para: {numero}')

    return HttpResponse('Mensagens enviadas')
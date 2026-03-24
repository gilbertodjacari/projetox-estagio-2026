from django.shortcuts import render, redirect
from .models import Cliente

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/lista_clientes.html', {'clientes': clientes})      

def adicionar_cliente(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        
        Cliente.objects.create(nome=nome, email=email, telefone=telefone)
        return redirect('lista_clientes')
    
    return render(request, 'clientes/adicionar_cliente.html')


from django.shortcuts import render, redirect
from .models import Cliente, Venda

def lista_vendas(request):
    vendas = Venda.objects.all()
    return render(request, 'vendas/lista_vendas.html', {'vendas': vendas})

def adicionar_venda(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        
        Cliente.objects.create(nome=nome, email=email, telefone=telefone)
        return redirect('lista_vendas')
    
    return render(request, 'vendas/adicionar_venda.html')


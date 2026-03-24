from django.shortcuts import render,redirect
from .models import Produto     

def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'cadastro/lista_produtos.html', {'produtos': produtos})

def cadastrar_produto(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        preco = request.POST.get('preco')
        
        Produto.objects.create(nome=nome, descricao=descricao, preco=preco)
        return redirect('lista_produtos')
    
    return render(request, 'cadastro/cadastrar_produto.html')


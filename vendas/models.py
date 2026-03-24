from django.db import models
from clientes.models import Cliente
from cadastro.models import Produto

# Create your models here.
class Venda(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    data_venda = models.DateTimeField(auto_now_add=True)    

    def __str__(self):
        return f"Venda de {self.produto.nome} para {self.cliente.nome} em {self.data_venda.strftime('%Y-%m-%d %H:%M:%S')}"
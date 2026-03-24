from django.urls import path
from . import views 

urlpatterns = [
    path('lista_vendas', views.lista_vendas, name='lista_vendas'),
    path('novo/', views.adicionar_venda, name='adicionar_venda'),

]   
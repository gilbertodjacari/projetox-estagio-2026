from django.urls import path
from . import views             

urlpatterns = [
    path('lista_produtos/', views.lista_produtos, name='lista_produtos'),
    path('novo/', views.cadastrar_produto, name='cadastrar_produto'),
]
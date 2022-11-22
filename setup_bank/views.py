import decimal
from django.shortcuts import render
from .models import Cartoes, Cliente, Conta, Emprestimos , Extrato, Transferencia
from .serializer import CartaoSerializer, ClienteSerializer, ContaSerializer, EmprestimoSerializer, ExtratoSerializer, TransfSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.shortcuts import render,get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from django_filters import rest_framework as filters
from django_filters.rest_framework import FilterSet


    

    
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    
class ContaViewSet(viewsets.ModelViewSet):
    queryset = Conta.objects.all()
    serializer_class = ContaSerializer
    def create(self, request, *args, **kwargs):
        conta = Conta.objects.filter(pk=1)
        print('qqc')
        
        for c in conta:
            # print(self.request.data['saldo'])
            contaAtual = Conta.objects.get(pk=c.pk)
            novoSaldo = {'saldo':self.request.data['saldo'],'numConta':self.request.data['numConta'], 'agencia':self.request.data['agencia']}
            # novoSaldo = {'saldo':3000,'numConta':2345, 'agencia':222}
            serializer = ContaSerializer(contaAtual,data=novoSaldo)
            if serializer.is_valid():
                serializer.save()
            print('for function')
        print('test',conta)
        if conta is None:
            
            return super().create(request, *args, **kwargs)
        else:
           return Response(status=status.HTTP_200_OK)
    
class TransfViewSet(viewsets.ModelViewSet):
    queryset = Transferencia.objects.all()
    serializer_class = TransfSerializer
    
class CartaoViewSet(viewsets.ModelViewSet):
    queryset = Cartoes.objects.all()
    serializer_class = CartaoSerializer  
    
class EmprestimoViewSet(viewsets.ModelViewSet):
    
    queryset = Emprestimos.objects.all()
    serializer_class = EmprestimoSerializer
    
    def somaSaldo(self):
        
        valor = Emprestimos.objects.get('valor_solicitado')
        valorSaldo =  Conta.objects.get('saldo')
        saldoNovo = valor + valorSaldo
        serializer = ContaSerializer(valorSaldo,data=saldoNovo)
        
        if serializer.is_valid():
            serializer.save()
        
        else:
           return Response(status=status.HTTP_200_OK)

        
  
class ExtratoViewSet(viewsets.ModelViewSet):
    queryset = Extrato.objects.all()
    serializer_class = ExtratoSerializer
    



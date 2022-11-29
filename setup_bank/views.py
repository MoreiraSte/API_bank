import decimal
from django.shortcuts import render
from .models import Cartoes, Cliente, Conta, Emprestimos , Transferencia
from .serializer import CartaoSerializer, ClienteSerializer, ContaSerializer, EmprestimoSerializer, TransfSerializer
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
    
    def create(self, request, *args, **kwargs):
        if self.request.data["operacao"] == 'logar':
            cliente = Cliente.objects.filter(email = self.request.data['email'],senha = self.request.data['senha'])[0]
            if cliente is not None:
                serializer = ClienteSerializer(cliente)
                
                return Response({'dados' : serializer.data})
            else:
                return Response(status=status.HTTP_401_OK)
        
        else:
            
           return super().create(request, *args, **kwargs)
    
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
    
    def create(self, request, *args, **kwargs):

        valor_transf = self.request.data['valor_transferencia']        
        conta_atual = Conta.objects.filter(pk=1)

        for e in conta_atual:
            contaAtual = Conta.objects.get(pk=e.pk)
            novo_valor = {'saldo': contaAtual.saldo - decimal.Decimal(valor_transf),'numConta': contaAtual.numConta, 'agencia':contaAtual.agencia}
            serializer_conta = ContaSerializer(contaAtual , data=novo_valor)
            if serializer_conta.is_valid():

                serializer_conta.save()
                
                  
                return super().create(request, *args, **kwargs)

            else:
                 return Response( {'message':serializer_conta.errors},status=status.HTTP_200_OK)
    
class CartaoViewSet(viewsets.ModelViewSet):
    queryset = Cartoes.objects.all()
    serializer_class = CartaoSerializer  
    
class EmprestimoViewSet(viewsets.ModelViewSet):
    
    queryset = Emprestimos.objects.all()
    serializer_class = EmprestimoSerializer
    
    def create(self, request, *args, **kwargs):

        valor_emprestimo = self.request.data['valor_solicitado']        
        conta_atual = Conta.objects.filter(pk=1)

        for e in conta_atual:
            contaAtual = Conta.objects.get(pk=e.pk)
            novo_valor = {'saldo': contaAtual.saldo + decimal.Decimal(valor_emprestimo),'numConta': contaAtual.numConta, 'agencia':contaAtual.agencia}
            serializer_conta = ContaSerializer(contaAtual , data=novo_valor)
            if serializer_conta.is_valid():

                serializer_conta.save()
                
                  
                return super().create(request, *args, **kwargs)

            else:
                 return Response( {'message':serializer_conta.errors},status=status.HTTP_200_OK)
    
   

        

    



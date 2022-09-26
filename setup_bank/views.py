from django.shortcuts import render
from .models import Cartoes, Cliente, Conta, Emprestimos, Endereco, Extrato, Faturas, PgtoEmprestimo, Transferencia, Usuario
from .serializer import CartaoSerializer, ClienteSerializer, ContaSerializer, EmprestimoSerializer, EnderecoSerializer, ExtratoSerializer, FaturaSerializer, PgtoEmprSerializer, TransfSerializer, UsuarioSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.shortcuts import render,get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets
from django_filters import rest_framework as filters
from django_filters.rest_framework import FilterSet


    
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    
class ContaViewSet(viewsets.ModelViewSet):
    queryset = Conta.objects.all()
    serializer_class = ContaSerializer
    
class TransfViewSet(viewsets.ModelViewSet):
    queryset = Transferencia.objects.all()
    serializer_class = TransfSerializer
    
class CartaoViewSet(viewsets.ModelViewSet):
    queryset = Cartoes.objects.all()
    serializer_class = CartaoSerializer
    
class FaturaViewSet(viewsets.ModelViewSet):
    queryset = Faturas.objects.all()
    serializer_class = FaturaSerializer
    
class EmprestimoViewSet(viewsets.ModelViewSet):
    queryset = Emprestimos.objects.all()
    serializer_class = EmprestimoSerializer
    
class PgtoEmprViewSet(viewsets.ModelViewSet):
    queryset = PgtoEmprestimo.objects.all()
    serializer_class = PgtoEmprSerializer
    
class ExtratoViewSet(viewsets.ModelViewSet):
    queryset = Extrato.objects.all()
    serializer_class = ExtratoSerializer
    
class EndViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer


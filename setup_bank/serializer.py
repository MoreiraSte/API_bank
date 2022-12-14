from rest_framework import serializers
from setup_bank.models import Cliente,Conta,Transferencia,Cartoes,Emprestimos
        
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cliente
        fields= ['id','nome', 'idade','genero', 'celular','data_nasc','email','cpf','senha','endereco']

        
class ContaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Conta
        fields= ['id','numConta','agencia','saldo']
        
class TransfSerializer(serializers.ModelSerializer):
    class Meta:
        model= Transferencia
        fields = ['id','tipo_transferencia','valor_transferencia','data_transferencia','recebeu_transf','enviou_transf']
        
class CartaoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cartoes
        fields= ['id', 'status_cartao']
        

        
class EmprestimoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Emprestimos
        fields=['id','valor_solicitado']
        
        

        

        
        


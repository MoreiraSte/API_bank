from rest_framework import serializers
from setup_bank.models import Usuario,Cliente,Endereco,Conta,Transferencia,Cartoes,Faturas,Emprestimos,PgtoEmprestimo,Extrat
        
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cliente
        fields= ['id','nome', 'idade','genero', 'celular','data_nasc','email','cpf','senha','foto', 'tipo']
        
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields= ['id','ususario']
        
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
        fields= ['id', 'status_cartao','numCartao','tipoClient','vencimento_cartao']
        
class FaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Faturas
        fields=['id','valor_fatura','data_vencimento','data_pagamento','vencimento_cartao']
        
class EmprestimoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Emprestimos
        fields=['id','status_emprestimo','valor_solicitado','data_solicitado','taxa_juros','qtd_parcelas','valor_com_juros','data_primeira_parcela','qtd_parcelas_pagas','valor_total_pago']
        
class PgtoEmprSerializer(serializers.ModelSerializer):
    class Meta:
        model=PgtoEmprestimo
        fields=['id', 'dataPgto','valor','emprestimo']
        
class ExtratoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Extrato
        fields=['id','status_extrato','data_extrato','conta']
        
class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Endereco
        fields=['id','cliente','rua','cidade','bairo','uf','numero','cep']
        
        


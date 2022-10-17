import email
from django.db import models
from django.core.validators import MinValueValidator
from django.forms import ImageField
#from pictures.models import PictureField

class Cliente(models.Model):
    
    FEMININO = 'F'
    MASCULINO = 'M'
    
    GENERO = [
        (FEMININO, 'Feminino'),
        (MASCULINO,'Masculino'),
        
    ]
    
    PLANO_PREMIUM = 'P'
    PLANO_FREE = 'F'
    
    TIPOS_PLANO = [
        (PLANO_FREE, 'Free'),
        (PLANO_PREMIUM,'Premium')
        
    ]
    
    genero= models.CharField(max_length=1, choices=GENERO,default=FEMININO)
    nome = models.CharField(max_length=255)
    idade = models.IntegerField(max_length=3)
    celular = models.CharField(max_length=15)
    data_nasc = models.DateField()
    email = models.CharField(max_length=255)
    cpf =  models.CharField(max_length=11)
    senha = models.IntegerField(validators=[MinValueValidator(8,"A senha precisa ter no minimo 8 caracteres")])
    foto = ImageField()
    tipo= models.CharField(max_length=1, choices=TIPOS_PLANO,default=PLANO_FREE)

class Usuario(models.Model):
    usuario = models.ForeignKey(Cliente,on_delete=models.PROTECT)
    
class Endereco(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    rua = models.CharField(max_length=255)
    cidade=models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    uf=models.CharField(max_length=2)
    numero=models.IntegerField(unique=True, max_length=6)
    cep =  models.IntegerField(max_length=9)
    
class Conta(models.Model):
    numConta = models.CharField(max_length=20)
    agencia = models.CharField(max_length=5)
    saldo = models.DecimalField(max_digits=8, decimal_places=2)
    
class Transferencia(models.Model):
    FORMA_PIX = 'P'
    FORMA_BOLETO = 'B'
    
    FORMA_PAGAMENTO = [
        (FORMA_PIX, 'Pix'),
        (FORMA_BOLETO, 'Boleto'),
    ]
    
    tipo_transferencia =  models.CharField(max_length=1, choices=FORMA_PAGAMENTO, default=FORMA_PIX)
    valor_transferencia = models.DecimalField(max_digits=8, decimal_places=2)
    data_transferencia = models.DateTimeField(auto_now_add=True)
    recebeu_transf = models.ForeignKey(Usuario,on_delete=models.CASCADE, related_name='recebeu_transf')
    enviou_transf = models.ForeignKey(Usuario,on_delete=models.CASCADE,related_name='enviou_transf')
    
class Cartoes(models.Model):
   
    CARTAO_FISICO = 'F'
    CARTAO_DIGITAL = 'D'
     
    CARTAO_OPCOES= [
        (CARTAO_FISICO,'Fisico'),
        (CARTAO_DIGITAL, 'Digital'),
    ]
    
    status_cartao = models.CharField(max_length=1, choices=CARTAO_OPCOES, default=CARTAO_DIGITAL)
    
    numCartao = models.CharField(max_length=16)
    tipoClient =models.ForeignKey(Usuario,on_delete=models.CASCADE)
    vencimento_cartao = models.DateField()
   
class Faturas(models.Model):
    valor_fatura = models.DecimalField(max_digits=8, decimal_places=2)
    data_vencimento = models.DateField()
    data_pagamento = models.DateField()
    vencimento_cartao = models.ForeignKey(Cartoes, on_delete=models.CASCADE)
    

class Emprestimos(models.Model):
    
    EMPRESTIMO_RECUSADO = 'R'
    EMPRESTIMO_AGUARDANDO = 'A'
    EMPRESTIMO_CONCLUIDO = 'C'
     
    SITUACAO= [
        (EMPRESTIMO_RECUSADO,'Recusado'),
        (EMPRESTIMO_AGUARDANDO, 'Aguardando'),
        (EMPRESTIMO_CONCLUIDO,'Concluido')
    ]
    
    status_emprestimo = models.CharField(max_length=1, choices=SITUACAO, default=EMPRESTIMO_AGUARDANDO)

    valor_solicitado = models.DecimalField(max_digits=8, decimal_places=2)
    data_solicitado = models.DateTimeField(auto_now_add=True)
    taxa_juros = models.IntegerField(max_length=2)
    qtd_parcelas = models.IntegerField(max_length=2)
    valor_com_juros = models.DecimalField(max_digits=8, decimal_places=2)
    data_primeira_parcela = models.DateTimeField(auto_now_add=True)
    qtd_parcelas_pagas = models.IntegerField(max_length=2)
    valor_total_pago = models.DecimalField(max_digits=8, decimal_places=2)


class PgtoEmprestimo(models.Model):
    dataPgto =  models.DateField(auto_now_add=True)
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    emprestimo = models.ForeignKey(Emprestimos, on_delete=models.CASCADE)

class Extrato(models.Model):
    
    TRANSFERENCIA = 'T'
    SAQUE = 'S'
    DEPOSITO = 'D'
    
    MODOS = [
        (TRANSFERENCIA,'transferencia'),
        (SAQUE,'saque'),
        (DEPOSITO,'deposito')
    ]
    
    status_extrato = models.CharField(max_length=1,choices=MODOS, default=SAQUE)
    
    data_extrato = models.DateField(auto_now_add=True)
    conta = models.ForeignKey(Conta,on_delete=models.PROTECT)
    transf = models.ForeignKey(Transferencia,on_delete=models.CASCADE)
    



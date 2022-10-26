import email
from django.db import models
from django.core.validators import MinValueValidator
from django.forms import ImageField
#from pictures.models import PictureField

class Cliente(models.Model):
    
    FEMININO = 'F'
    MASCULINO = 'M'
    
    SAO_PAULO = 'SP'
    ACRE = 'AC'
    ALAGOAS = 'AL'
    AMAPA ='AP'
    AMAZONAS='AM'
    BAHIA = 'BA'
    CEARA = 'CE'
    ESPIRITO_SANTO = 'ES'
    GOIAS = 'GO'
    MARANHAO = 'MA'
    MATO_GROSSO = 'MT'
    MATO_GROSSO_SUL = 'MS'
    MINAS_GERAIS='MG'
    PARA='PA'
    PARAIBA='PB'
    PARANA='PR'
    PERNAMBUCO='PE'
    PIAUI='PI'
    RIO_JANEIRO='RJ'
    RIO_GRANDE_NORTE='RN'
    RIO_GRANDE_SUL='RS'
    RONDONIA='RO'
    RORAIMA='RR'
    SANTA_CATARINA='SC'
    SERGIPE='SE'
    TOCANTINS='TO'
    DISTRITO = 'DF'
    
    GENERO = [
        (FEMININO, 'Feminino'),
        (MASCULINO,'Masculino'),
        
    ]
    
   
    ESTADOS = [
        (SAO_PAULO, 'SAO PAULO'),
        (ACRE, 'ACRE'),
        (ALAGOAS, 'ALAGOAS'),
        (AMAPA, 'AMAPA'),
        (AMAZONAS, 'AMAZONAS'),
        (BAHIA, 'BAHIA'),
        (CEARA, 'CEARA'),
        (ESPIRITO_SANTO, 'ESPIRITO SANTO'),
        (GOIAS, 'GOIAS'),
        (MARANHAO, 'MARANHAO'),
        (MATO_GROSSO, 'MATO GROSSO'),
        (MATO_GROSSO_SUL, 'MATO GROSSO DO SUL'),
        (MINAS_GERAIS, 'MINAS GERAIS'),
        (PARA, 'PARA'),
        (PARAIBA, 'PARAIBA'),
        (PARANA, 'PARANA'),
        (PERNAMBUCO, 'PERNAMBUCO'),
        (PIAUI, 'PIAUI'),
        (RIO_JANEIRO, 'RIO DE JANEIRO'),
        (RIO_GRANDE_NORTE, 'RIO GRANDE DO NORTE'),
        (RIO_GRANDE_SUL, 'RIO GRANDE DO SUL'),
        (RONDONIA, 'RONDONIA'),
        (RORAIMA, 'RORAIMA'),
        (SANTA_CATARINA, 'SANTA CATARINA'),
        (SERGIPE, 'SERGIPE'),
        (TOCANTINS, 'TOCANTINS'),
        (DISTRITO, 'DISTRITO'),
    ]
    endereco =  models.CharField(max_length=2, choices=ESTADOS, default=SAO_PAULO)
    genero= models.CharField(max_length=1, choices=GENERO,default=FEMININO)
    nome = models.CharField(max_length=255)
    idade = models.IntegerField(max_length=3)
    celular = models.CharField(max_length=15)
    data_nasc = models.DateField()
    email = models.CharField(max_length=255)
    cpf =  models.CharField(max_length=11)
    senha = models.IntegerField(validators=[MinValueValidator(8,"A senha precisa ter no minimo 8 caracteres")])
    foto = ImageField()
   

class Usuario(models.Model):
    usuario = models.ForeignKey(Cliente,on_delete=models.PROTECT)
    
    
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
    



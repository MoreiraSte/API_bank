# Generated by Django 4.1.1 on 2022-10-26 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setup_bank', '0003_remove_cliente_tipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='endereco',
            field=models.CharField(choices=[('SP', 'SAO PAULO'), ('AC', 'ACRE'), ('AL', 'ALAGOAS'), ('AP', 'AMAPA'), ('AM', 'AMAZONAS'), ('BA', 'BAHIA'), ('CE', 'CEARA'), ('ES', 'ESPIRITO SANTO'), ('GO', 'GOIAS'), ('MA', 'MARANHAO'), ('MT', 'MATO GROSSO'), ('MS', 'MATO GROSSO DO SUL'), ('MG', 'MINAS GERAIS'), ('PA', 'PARA'), ('PB', 'PARAIBA'), ('PR', 'PARANA'), ('PE', 'PERNAMBUCO'), ('PI', 'PIAUI'), ('RJ', 'RIO DE JANEIRO'), ('RN', 'RIO GRANDE DO NORTE'), ('RS', 'RIO GRANDE DO SUL'), ('RO', 'RONDONIA'), ('RR', 'RORAIMA'), ('SC', 'SANTA CATARINA'), ('SE', 'SERGIPE'), ('TO', 'TOCANTINS'), ('DF', 'DISTRITO')], default='SP', max_length=2),
        ),
        migrations.DeleteModel(
            name='Endereco',
        ),
    ]

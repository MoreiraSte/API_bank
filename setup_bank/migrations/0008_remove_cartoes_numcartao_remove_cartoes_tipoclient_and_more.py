# Generated by Django 4.1.3 on 2022-11-17 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setup_bank', '0007_alter_cartoes_tipoclient_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartoes',
            name='numCartao',
        ),
        migrations.RemoveField(
            model_name='cartoes',
            name='tipoClient',
        ),
        migrations.RemoveField(
            model_name='cartoes',
            name='vencimento_cartao',
        ),
        migrations.DeleteModel(
            name='Faturas',
        ),
    ]

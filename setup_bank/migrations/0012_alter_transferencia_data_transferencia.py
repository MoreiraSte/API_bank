# Generated by Django 4.1.3 on 2022-11-28 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setup_bank', '0011_delete_extrato'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transferencia',
            name='data_transferencia',
            field=models.CharField(max_length=255),
        ),
    ]

# Generated by Django 3.2.24 on 2024-05-07 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fuel', '0023_alter_abastecimento_litros_abastecidos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abastecimento',
            name='km_final',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='abastecimento',
            name='km_inicial',
            field=models.IntegerField(),
        ),
    ]

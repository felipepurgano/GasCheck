# Generated by Django 3.2.24 on 2024-04-13 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fuel', '0022_alter_cadcarros_ano'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abastecimento',
            name='litros_abastecidos',
            field=models.FloatField(),
        ),
    ]

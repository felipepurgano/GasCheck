# Generated by Django 3.2.24 on 2024-05-19 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fuel', '0024_auto_20240506_2131'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consumo_carros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=50)),
                ('consumo_cidade', models.CharField(max_length=50)),
                ('consumo_estrada', models.CharField(max_length=50)),
            ],
        ),
    ]

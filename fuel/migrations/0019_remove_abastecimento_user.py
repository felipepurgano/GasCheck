# Generated by Django 3.2.24 on 2024-04-13 02:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fuel', '0018_remove_cadcarros_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='abastecimento',
            name='user',
        ),
    ]
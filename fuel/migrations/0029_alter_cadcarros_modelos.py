# Generated by Django 3.2.24 on 2024-05-19 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fuel', '0028_rename_modelo_cadcarros_modelos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadcarros',
            name='modelos',
            field=models.CharField(max_length=20),
        ),
    ]

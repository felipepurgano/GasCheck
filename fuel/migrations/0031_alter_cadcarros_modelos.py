# Generated by Django 3.2.24 on 2024-05-19 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fuel', '0030_auto_20240519_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadcarros',
            name='modelos',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='fuel.consumo_carros'),
        ),
    ]

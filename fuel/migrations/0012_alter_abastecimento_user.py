# Generated by Django 3.2.24 on 2024-04-13 01:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fuel', '0011_alter_cadcarros_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abastecimento',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]

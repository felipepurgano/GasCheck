# Generated by Django 3.2.24 on 2024-04-13 01:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fuel', '0010_auto_20240412_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadcarros',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]

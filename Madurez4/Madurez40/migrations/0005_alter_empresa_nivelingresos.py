# Generated by Django 4.1 on 2022-10-21 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Madurez40', '0004_rename_tamañodeempresa_empresa_tamanodeempresa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='NivelIngresos',
            field=models.FloatField(default=0),
        ),
    ]

# Generated by Django 4.1 on 2022-11-01 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Madurez40', '0006_alter_empresa_costodirecto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='reto1',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='reto2',
            field=models.PositiveIntegerField(default=2),
        ),
    ]
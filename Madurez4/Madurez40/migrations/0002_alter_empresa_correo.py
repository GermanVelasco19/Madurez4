# Generated by Django 4.1 on 2022-09-27 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Madurez40', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='Correo',
            field=models.EmailField(max_length=254),
        ),
    ]

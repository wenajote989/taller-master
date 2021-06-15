# Generated by Django 3.2.3 on 2021-06-13 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_contacto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo_auto', models.CharField(max_length=25)),
                ('patente_auto', models.CharField(max_length=7)),
            ],
        ),
        migrations.AlterField(
            model_name='contacto',
            name='apellido_cont',
            field=models.CharField(max_length=45, verbose_name='Apellidos'),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='modelo_cont',
            field=models.CharField(max_length=35, verbose_name='Modelo vehiculo'),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='nombre_cont',
            field=models.CharField(max_length=25, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='patente_cont',
            field=models.CharField(max_length=6, verbose_name='Patente'),
        ),
    ]
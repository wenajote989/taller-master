# Generated by Django 3.2.3 on 2021-06-12 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_cont', models.CharField(max_length=25)),
                ('apellido_cont', models.CharField(max_length=45)),
                ('modelo_cont', models.CharField(max_length=35)),
                ('patente_cont', models.CharField(max_length=6)),
                ('email_cont', models.EmailField(max_length=254)),
                ('mensaje_cont', models.TextField()),
            ],
        ),
    ]

# Generated by Django 3.2.3 on 2021-06-07 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mecanico',
            fields=[
                ('idCategoria', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id Categoria')),
                ('nombre_mec', models.CharField(max_length=50, verbose_name='Nombre mec')),
                ('apellido_sol', models.CharField(max_length=20, verbose_name='Apellido mec')),
            ],
        ),
    ]

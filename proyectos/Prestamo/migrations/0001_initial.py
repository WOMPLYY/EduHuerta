# Generated by Django 4.2.4 on 2023-09-19 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Herramienta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disponibilidad', models.CharField(choices=[('disponible', 'Disponible'), ('no disponible', 'Nodisponible')], max_length=15, verbose_name='Disponibilidad')),
                ('descripcion', models.TextField(verbose_name='Descripcion')),
            ],
            options={
                'verbose_name': 'Herramienta',
                'verbose_name_plural': 'Herramientas',
                'db_table': 'herramienta',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(choices=[('activo', 'Activo'), ('inactivo', 'Inactivo')], max_length=20, verbose_name='Estado')),
                ('descripcion', models.TextField(verbose_name='Descripcion')),
                ('cantidad', models.IntegerField(verbose_name='Cantidad')),
            ],
            options={
                'verbose_name': 'Prestamo',
                'verbose_name_plural': 'Prestamos',
                'db_table': 'prestamo',
                'ordering': ['id'],
            },
        ),
    ]
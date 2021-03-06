# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-05 13:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150, verbose_name='Nombre de la Empresa')),
                ('titularempresa', models.CharField(max_length=150, verbose_name='Titular de la Empresa')),
                ('giro', models.CharField(max_length=100, verbose_name='Giro de la Empresa')),
                ('titularproyecto', models.CharField(max_length=150, verbose_name='Titular del Proyecto')),
                ('direccion', models.CharField(max_length=255, verbose_name='Calle y Numero')),
                ('colonia', models.CharField(max_length=255, verbose_name='Colonia')),
                ('codigo_postal', models.CharField(max_length=50, verbose_name='Codigo Postal')),
                ('rfc', models.CharField(max_length=100, verbose_name='RFC')),
                ('telefono', models.CharField(max_length=50, verbose_name='Telefono')),
                ('email', models.CharField(max_length=100, verbose_name='Email')),
                ('social', models.CharField(max_length=255, verbose_name='Redes Sociales')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.RemoveField(
            model_name='alumno',
            name='matricula',
        ),
        migrations.RemoveField(
            model_name='carrera',
            name='published_date',
        ),
        migrations.RemoveField(
            model_name='proyecto',
            name='carrera',
        ),
        migrations.RemoveField(
            model_name='proyecto',
            name='published_date',
        ),
        migrations.AddField(
            model_name='proyecto',
            name='estado',
            field=models.CharField(default=1, max_length=10, verbose_name='Proyecto: Asignado o NO Asignado'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='proyecto',
            name='matricula',
            field=models.CharField(default=1, max_length=10, verbose_name='Matricula Asignada'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='carrera',
            name='nombre',
            field=models.CharField(max_length=150, verbose_name='Nombre Carrera'),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='descripcion',
            field=models.CharField(max_length=255, verbose_name='Descripcion del proyecto'),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='empresa',
            field=models.CharField(max_length=150, verbose_name='Nombre de la Institucion o Empresa'),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='nombre',
            field=models.CharField(max_length=150, verbose_name='Nombre proyecto'),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='tipo_proyecto',
            field=models.CharField(max_length=1, verbose_name='Proyecto: INTERNO o EXTERNO'),
        ),
        migrations.DeleteModel(
            name='Alumno',
        ),
    ]

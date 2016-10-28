# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-27 15:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edad', models.IntegerField()),
                ('tel', models.CharField(max_length=13)),
                ('genero', models.CharField(choices=[('hombre', 'HOMBRE'), ('mujer', 'MUJER')], max_length=6)),
                ('alias', models.CharField(max_length=10)),
                ('domicilio', models.TextField()),
                ('ocupacion', models.CharField(choices=[('estudiante', 'Estudiante'), ('academico', 'Academico'), ('publico', 'Servidor Público'), ('empresario', 'Empresario'), ('godinez', 'Empleado')], max_length=140)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

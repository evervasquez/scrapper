# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-09 06:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ruc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('Provincia', models.CharField(blank=True, max_length=100, null=True)),
                ('Condicion', models.CharField(blank=True, max_length=100, null=True)),
                ('Ruc', models.CharField(blank=True, max_length=100, null=True)),
                ('Departamento', models.CharField(blank=True, max_length=100, null=True)),
                ('Domicilio', models.CharField(blank=True, max_length=100, null=True)),
                ('Distrito', models.CharField(blank=True, max_length=100, null=True)),
                ('Estado', models.CharField(blank=True, max_length=100, null=True)),
                ('Ubigeo', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]

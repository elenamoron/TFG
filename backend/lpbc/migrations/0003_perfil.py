# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 09:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lpbc', '0002_auto_20171025_1051'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100)),
                ('apellidos', models.CharField(blank=True, max_length=255)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('codigo_postal', models.CharField(blank=True, max_length=10)),
                ('telefono', models.CharField(blank=True, max_length=20)),
                ('mail', models.CharField(blank=True, max_length=255)),
                ('observaciones', models.TextField(blank=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Perfiles',
                'verbose_name': 'Perfil',
            },
        ),
    ]

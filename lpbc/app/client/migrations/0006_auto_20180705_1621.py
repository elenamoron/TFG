# Generated by Django 2.0.3 on 2018-07-05 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0005_auto_20180704_1524'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='physicalperson',
            options={'ordering': ('name',)},
        ),
    ]

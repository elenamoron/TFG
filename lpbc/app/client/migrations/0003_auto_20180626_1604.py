# Generated by Django 2.0.3 on 2018-06-26 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_auto_20180626_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='physicalperson',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='organization.Project'),
        ),
    ]

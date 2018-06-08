# Generated by Django 2.0.3 on 2018-05-21 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
        ('client', '0005_auto_20180516_1440'),
    ]

    operations = [
        migrations.CreateModel(
            name='SupportDoc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_justificacion', models.CharField(blank=True, max_length=255)),
                ('persona_fisica', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='client.PhysicalPerson')),
                ('persona_juridica', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='client.LegalPerson')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='organization.Project')),
            ],
        ),
        migrations.RenameField(
            model_name='document',
            old_name='meta_descripcion',
            new_name='content_type',
        ),
        migrations.RemoveField(
            model_name='document',
            name='persona_fisica',
        ),
        migrations.RemoveField(
            model_name='document',
            name='persona_juridica',
        ),
        migrations.RemoveField(
            model_name='document',
            name='project',
        ),
        migrations.AddField(
            model_name='document',
            name='length',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
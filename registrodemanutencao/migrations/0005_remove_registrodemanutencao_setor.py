# Generated by Django 5.1.1 on 2024-10-15 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registrodemanutencao', '0004_alter_registrodemanutencao_customizacaoo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registrodemanutencao',
            name='setor',
        ),
    ]

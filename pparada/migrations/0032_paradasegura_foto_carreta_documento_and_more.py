# Generated by Django 5.1.2 on 2024-10-30 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pparada', '0031_paradasegura_saida_alter_paradasegura_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='paradasegura',
            name='foto_carreta_documento',
            field=models.ImageField(blank=True, null=True, upload_to='fotos_carreta_documento/'),
        ),
        migrations.AddField(
            model_name='paradasegura',
            name='foto_documento_cavalo',
            field=models.ImageField(blank=True, null=True, upload_to='fotos_cavalo/'),
        ),
        migrations.AddField(
            model_name='paradasegura',
            name='foto_documento_motorista',
            field=models.ImageField(blank=True, null=True, upload_to='fotos_motorista_documento/'),
        ),
    ]
# Generated by Django 5.1.2 on 2024-10-30 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pparada', '0029_paradasegura_foto_carreta_paradasegura_foto_cavalo'),
    ]

    operations = [
        migrations.AddField(
            model_name='paradasegura',
            name='status',
            field=models.CharField(blank=True, default='EM VIAGEM', max_length=50, null=True),
        ),
    ]

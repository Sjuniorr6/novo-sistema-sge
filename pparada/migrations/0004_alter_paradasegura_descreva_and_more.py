# Generated by Django 5.1.1 on 2024-10-14 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pparada', '0003_alter_paradasegura_descreva'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paradasegura',
            name='descreva',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='paradasegura',
            name='tipo_posto',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='Pendente', max_length=255, null=True),
        ),
    ]

# Generated by Django 5.1.1 on 2024-10-07 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrodemanutencao', '0002_alter_registrodemanutencao_faturamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrodemanutencao',
            name='entregue_por_retirado_por',
            field=models.CharField(choices=[('Correios/Transportadora', 'Correios/Transportadora'), ('Entrega na base', 'Entrega na base'), ('Motoboy', 'Motoboy')], default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='registrodemanutencao',
            name='recebimento',
            field=models.CharField(blank=True, choices=[('Correios/Transportadora', 'Correios/Transportadora'), ('Entrega na base', 'Entrega na base'), ('Motoboy', 'Motoboy')], max_length=50, null=True),
        ),
    ]

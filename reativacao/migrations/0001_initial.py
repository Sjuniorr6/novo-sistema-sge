# Generated by Django 5.1.1 on 2024-10-24 18:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('acompanhamento', '0003_rename_transportadora_clientes_seguradora'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reativacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivo_reativacao', models.CharField(blank=True, choices=[('Retornavel', 'Retornavel'), ('Descartavel', 'Descartavel')], max_length=50, null=True)),
                ('canal_solicitacao', models.CharField(blank=True, max_length=100, null=True)),
                ('observacoes', models.CharField(max_length=100)),
                ('status_reativacao', models.CharField(choices=[('Faturado', 'Faturado'), ('Não Faturado', 'Não Faturado')], default='Não Faturado', max_length=100)),
                ('nome', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reativacao_nome', to='acompanhamento.clientes')),
            ],
        ),
        migrations.CreateModel(
            name='IdIccid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_equipamentos', models.CharField(blank=True, default='', max_length=300)),
                ('ccid_equipamentos', models.CharField(blank=True, default='', max_length=300)),
                ('quantidade', models.PositiveIntegerField(default=0)),
                ('reativacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_iccids', to='reativacao.reativacao')),
            ],
        ),
    ]

# Generated by Django 5.1.1 on 2024-10-28 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reativacao', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reativacao',
            name='data',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]

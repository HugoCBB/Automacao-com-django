# Generated by Django 5.1.3 on 2025-03-03 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0004_alter_cliente_matriculado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='matriculado',
            field=models.CharField(choices=[('Não Matriculado', 'Não Matriculado'), ('Matriculado', 'Matriculado')], default='Não Matriculado', max_length=15),
        ),
    ]

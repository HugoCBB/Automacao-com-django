# Generated by Django 5.1.3 on 2024-12-20 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_alter_mensagem_mensagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='matriculado',
            field=models.CharField(choices=[('Matriculado', 'Matriculado'), ('Não Matriculado', 'Não Matriculado')], default='Não Matriculado', max_length=15),
        ),
    ]

# Generated by Django 2.2.7 on 2020-09-21 03:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0003_pedido_tipopago'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='nope',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='clave',
            field=models.CharField(max_length=4, unique=True, validators=[django.core.validators.RegexValidator(code='nomatch', message='El # ingresado es invalido, Debe tener 4 caracteres', regex='^.{4}$')]),
        ),
    ]
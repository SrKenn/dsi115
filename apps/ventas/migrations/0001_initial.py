# Generated by Django 2.2.7 on 2020-09-20 05:35

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventario', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=40)),
                ('apellidos', models.CharField(max_length=40)),
                ('telefono', models.CharField(max_length=8, unique=True, validators=[django.core.validators.RegexValidator(code='nomatch', message='El # ingresado es invalido, Debe tener 8 caracteres', regex='^.{8}$')])),
                ('dui', models.CharField(max_length=9, unique=True, validators=[django.core.validators.RegexValidator(code='nomatch', message='El DUI ingresado es invalido, Debe tener 9 caracteres', regex='^.{9}$')])),
                ('nit', models.CharField(max_length=14, unique=True, validators=[django.core.validators.RegexValidator(code='nomatch', message='El NIT ingresado es invalido, Debe tener 14 caracteres', regex='^.{14}$')])),
            ],
        ),
        migrations.CreateModel(
            name='Metas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto_asignado', models.DecimalField(decimal_places=2, max_digits=6)),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('finalizada', models.BooleanField(default=False)),
                ('fechaCreada', models.DateField(auto_now=True)),
                ('cliente', models.CharField(max_length=50, null=True)),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('vendedor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ventas.Empleado')),
            ],
        ),
        migrations.CreateModel(
            name='lineaDeVenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=1)),
                ('subtotal', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('articulofk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.Producto')),
                ('pedidofk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.pedido')),
            ],
        ),
        migrations.AddField(
            model_name='empleado',
            name='meta_asignadafk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ventas.Metas'),
        ),
        migrations.AddField(
            model_name='empleado',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Asignacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_asignacion', models.DateField(auto_now=True)),
                ('monto_logrado', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=6)),
                ('empleadofk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.Empleado')),
                ('meta_asignadafk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.Metas')),
            ],
            options={
                'unique_together': {('empleadofk', 'meta_asignadafk')},
            },
        ),
    ]

from apps.inventario.models import *
from django import forms

from django.forms import widgets
from django.forms import fields, CheckboxInput

class productoForm(forms.ModelForm):
	fkcate = forms.ModelChoiceField(queryset=CategoriaIncidencia.objects.all())
	comentario = forms.CharField(required=False, max_length=150)
	class Meta:
		model=Producto
		fields=[
			'nombre',
			'descripcion',
			'precioventa',
			'preciocompra',
			'existencia',
			'promocion',
			'fkcategoria',
			'fkproveedor',
			]
		labels={

			'nombre':'Nombre',
			'descripcion':'Descripcion:',
			'precioventa':'Precio de Venta:',
			'preciocompra':'Precio de Compra:',
			'existencia':'Existencias:',
			'promocion':'Promocion:',
			'fkcategoria':'Categoria',
			'fkproveedor':'Proveedor',
		}
		widgets={
			'nombre': forms.TextInput(),
			'descripcion': forms.TextInput(),
			'precioventa': forms.NumberInput(),
			'preciocompra': forms.NumberInput(),
			'existencia': forms.TextInput(),
			'promocion': forms.CheckboxInput(),
			'fkproveedor': forms.Select(),
			'fkcategoria': forms.Select(),
		}


class elimiarForm(forms.Form):
	confirmar = forms.CheckboxInput()
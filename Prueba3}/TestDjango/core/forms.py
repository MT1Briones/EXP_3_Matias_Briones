
from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Categoria, Producto, Categoria2, Cliente


class ProductoForm (forms.ModelForm):
    class Meta: 
        model= Producto
        fields = ['idProducto','nombre','precio' , 'categoria']
        labels ={
            'idProducto': 'Idproducto', 
            'nombre': 'Nombre', 
            'precio':'Precio',
            'categoria': 'Categoria',
        }
        widgets={
            'idProducto': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese id', 
                    'id': 'idProducto'
                }
            ), 
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese nombre', 
                    'id': 'nombre'
                }
            ), 
            'precio': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese precio', 
                    'id': 'precio'
                }
            ),
            'categoria': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'categoria',
                }
            ),
        },
        
class ClienteForm (forms.ModelForm):
    class Meta: 
        model= Cliente
        fields = ['idCliente','nombre2','edad' , 'categoria2']
        labels ={
            'idCliente': 'Idcliente', 
            'nombre2': 'Nombre2', 
            'edad':'Edad',
            'categoria2': 'Categoria2',
        }
        widgets={
            'idCliente': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese id', 
                    'id': 'idCliente'
                }
            ), 
            'nombre2': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese nombre', 
                    'id': 'nombre2'
                }
            ), 
            'edad': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese precio', 
                    'id': 'edad'
                }
            ),
            'categoria2': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'categoria2',
                }
            ),
        }
from django.db import models

# Create your models here.
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de Categoria')
    nombreCategoria=models.CharField(max_length=50, verbose_name='Nombre de Categoria')

    def __str__(self): 
        return self.nombreCategoria


class Producto (models.Model): 
    idProducto = models.CharField(primary_key=True, max_length=6, verbose_name='Idproducto')
    nombre= models.CharField(max_length=50, verbose_name='Nombre')
    precio= models.CharField(max_length=20, verbose_name='Precio')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name='Categoria')

    def __str__(self):
        return self.idProducto

class Categoria2(models.Model):
    idCategoria2 = models.IntegerField(primary_key=True, verbose_name='Id de Categoria')
    nombreCategoria2 =models.CharField(max_length=50, verbose_name='Nombre de Categoria')

    def __str__(self): 
        return self.nombreCategoria2


class Cliente (models.Model): 
    idCliente = models.CharField(primary_key=True, max_length=6, verbose_name='Idcliente')
    nombre2= models.CharField(max_length=50, verbose_name='Nombre2')
    edad= models.CharField(max_length=20, verbose_name='Edad')
    categoria2 = models.ForeignKey(Categoria2, on_delete=models.CASCADE, verbose_name='Categoria2')

    def __str__(self):
        return self.idCliente

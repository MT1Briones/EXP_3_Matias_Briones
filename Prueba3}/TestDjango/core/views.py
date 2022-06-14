from django.shortcuts import render, redirect
from .models import Producto, Cliente
from .forms import ProductoForm, ClienteForm


# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')


def quienes(request): 
    return render (request, 'quienesSomos.html') 

def galeria(request):
    return render(request, 'galeria.html')


def FORMULARIO1(request): 
    return render (request, 'FORMULARIO1.html') 

def Contacto(request):
    return render(request, 'Contacto.html')


def api(request): 
    return render (request, 'api.html') 


def mostrar (request):
    productos = Producto.objects.all()

    datos = {
        'productos': productos
    }
    return render(request, 'mostrar.html', datos)
def mostrar2 (request):
    clientes = Cliente.objects.all()

    datos = {
        'clientes': clientes
    }
    return render(request, 'mostrar2.html', datos)
def form_crear_clientes(request):
    if request.method=='POST': 
        cliente_form = ClienteForm(request.POST)
        if cliente_form.is_valid():
            cliente_form.save()
            return redirect('inicio')
    else:
        cliente_form= ClienteForm()
    return render(request, 'form_crear_clientes.html', {'cliente_form':  cliente_form})

def form_mod_clientes(request, id): 
    cliente = Cliente.objects.get(idCliente=id)
    datos = {
        'form':   ClienteForm(instance=cliente)
    }
    if request.method=='POST':
        formulario =   ClienteForm(data = request.POST, instance=cliente)
        if formulario.is_valid: 
            formulario.save()
            return redirect ('mostrar2')
    return render (request, 'form_mod_clientes.html', datos)

def form_del_Cliente(request, id):
    cliente = Cliente.objects.get(idCliente=id)
    cliente.delete()
    return redirect ('mostrar2')

def form_crear_productos(request):
    if request.method=='POST': 
        producto_form = ProductoForm(request.POST)
        if producto_form.is_valid():
            producto_form.save()
            return redirect('inicio')
    else:
        producto_form= ProductoForm()
    return render(request, 'form_crear_productos.html', {'producto_form': producto_form})

def form_mod_Producto(request, id): 
    producto = Producto.objects.get(idProducto=id)
    datos = {
        'form':  ProductoForm(instance=producto)
    }
    if request.method=='POST':
        formulario =  ProductoForm(data = request.POST, instance=producto)
        if formulario.is_valid: 
            formulario.save()
            return redirect ('mostrar')
    return render (request, 'form_mod_Productos.html', datos )

def form_del_Producto(request, id):
    producto = Producto.objects.get(idProducto=id)
    producto.delete()
    return redirect ('mostrar')
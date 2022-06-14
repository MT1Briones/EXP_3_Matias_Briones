from django.urls import path 
from .views import  inicio, quienes, galeria, Contacto, FORMULARIO1, api, form_del_Producto, form_mod_Producto, form_crear_productos, mostrar, mostrar2, form_crear_clientes, form_mod_clientes, form_del_Cliente

urlpatterns=[
    path('',inicio, name="inicio"),
    path('quienesSomos/',quienes, name="quienes"), 
    path('galeria/',galeria, name="galeria"), 
    path('Contacto/',Contacto, name="Contacto"), 
    path('FORMULARIO1/',FORMULARIO1, name="FORMULARIO1"), 
    path('api/',api, name="api"), 
    path ('form_crear_productos/', form_crear_productos, name="form_crear_productos"),
    path ('mostrar/' , mostrar , name="mostrar"),
    path ('form_crear_clientes/', form_crear_clientes, name="form_crear_clientes"),
    path ('form_mod_clientes/<id>', form_mod_clientes, name="form_mod_clientes"),
    path ('form_del_Cliente/<id>', form_del_Cliente, name="form_del_Cliente"),
    path ('mostrar2/' , mostrar2 , name="mostrar2"),
    path ('form_mod_Producto/<id>', form_mod_Producto, name="form_mod_Producto"),
    path ('form_del_Producto/<id>', form_del_Producto, name="form_del_Producto"),
]
from django.shortcuts import render
from django.http import HttpResponse
from .models import Producto
from .forms import ProductoForm

def crear_producto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        precio = request.POST.get('precio')
        descripcion = request.POST.get('descripcion')
        producto = Producto(nombre=nombre, precio=precio, descripcion=descripcion)
        producto.save()
        return HttpResponse('Producto creado exitosamente!')
    else:
        return render(request, 'crear_producto.html')

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'listar_productos.html', {'productos': productos})

def productos_caros(request):
    productos_caros = Producto.objects.filter(precio__gt=5000)
    return render(request, 'productos_caros.html', {'productos_caros': productos_caros})

def actualizar_producto(request, producto_id):
    producto = Producto.objects.get(pk=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return HttpResponse('Producto actualizado exitosamente!')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'actualizar_producto.html', {'form': form, 'producto': producto})

def eliminar_producto(request, producto_id):
    producto = Producto.objects.get(pk=producto_id)
    producto.delete()
    return HttpResponse('Producto eliminado exitosamente!')
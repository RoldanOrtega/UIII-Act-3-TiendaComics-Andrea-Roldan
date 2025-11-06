from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Proveedor, Cliente

def inicio_comics(request):
    return render(request, 'inicio.html')

# VISTAS PARA PRODUCTO
def agregar_Producto(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        autor = request.POST['autor']
        editorial = request.POST['editorial']
        genero = request.POST['genero']
        precio = request.POST['precio']
        stock = request.POST['stock']
        fecha_publicacion = request.POST['fecha_publicacion']
        isbn = request.POST['isbn']
        tipo_producto = request.POST['tipo_producto']
        proveedor_id = request.POST['proveedor']
        
        proveedor = Proveedor.objects.get(id=proveedor_id)
        
        Producto.objects.create(
            nombre=nombre,
            autor=autor,
            editorial=editorial,
            genero=genero,
            precio=precio,
            stock=stock,
            fecha_publicacion=fecha_publicacion,
            isbn=isbn,
            tipo_producto=tipo_producto,
            proveedor=proveedor
        )
        return redirect('ver_Productos')
    
    proveedores = Proveedor.objects.all()
    return render(request, 'Producto/agregar_Productos.html', {'proveedores': proveedores})

def ver_Productos(request):
    productos = Producto.objects.all()
    return render(request, 'Producto/ver_Productos.html', {'productos': productos})

def actualizar_Producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    proveedores = Proveedor.objects.all()
    return render(request, 'Producto/actualizar_Productos.html', {
        'producto': producto,
        'proveedores': proveedores
    })

def realizar_actualizacion_Producto(request, producto_id):
    if request.method == 'POST':
        producto = get_object_or_404(Producto, id=producto_id)
        
        producto.nombre = request.POST['nombre']
        producto.autor = request.POST['autor']
        producto.editorial = request.POST['editorial']
        producto.genero = request.POST['genero']
        producto.precio = request.POST['precio']
        producto.stock = request.POST['stock']
        producto.fecha_publicacion = request.POST['fecha_publicacion']
        producto.isbn = request.POST['isbn']
        producto.tipo_producto = request.POST['tipo_producto']
        producto.proveedor_id = request.POST['proveedor']
        
        producto.save()
        return redirect('ver_Productos')

def borrar_Producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'Producto/borrar_Productos.html', {'producto': producto})

def confirmar_borrar_Producto(request, producto_id):
    if request.method == 'POST':
        producto = get_object_or_404(Producto, id=producto_id)
        producto.delete()
        return redirect('ver_Productos')
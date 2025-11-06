from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_comics, name='inicio_comics'),
    
    # URLs para Producto
    path('productos/agregar/', views.agregar_Producto, name='agregar_Producto'),
    path('productos/', views.ver_Productos, name='ver_Productos'),
    path('productos/actualizar/<int:producto_id>/', views.actualizar_Producto, name='actualizar_Producto'),
    path('productos/realizar_actualizacion/<int:producto_id>/', views.realizar_actualizacion_Producto, name='realizar_actualizacion_Producto'),
    path('productos/borrar/<int:producto_id>/', views.borrar_Producto, name='borrar_Producto'),
    path('productos/confirmar_borrar/<int:producto_id>/', views.confirmar_borrar_Producto, name='confirmar_borrar_Producto'),
]
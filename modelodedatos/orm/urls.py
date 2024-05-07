from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.crear_producto, name='crear_producto'),
    path('listar/', views.listar_productos, name='listar_productos'),
    path('productos_caros/', views.productos_caros, name='productos_caros'),
    path('actualizar/<int:producto_id>/', views.actualizar_producto, name='actualizar_producto'),
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
]
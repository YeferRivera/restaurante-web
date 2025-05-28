from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('platos/crear/', views.crear_plato, name='crear_plato'),
    path('platos/<int:plato_id>/editar/', views.editar_plato, name='editar_plato'),
    path('platos/<int:plato_id>/eliminar/', views.eliminar_plato, name='eliminar_plato'),
    # Órdenes
    path('ordenes/', views.listar_ordenes, name='listar_ordenes'),
    path('ordenes/crear/', views.crear_orden, name='crear_orden'),
    path('ordenes/<int:orden_id>/', views.detalle_orden, name='detalle_orden'),
     # ... otras rutas ...
    path('pagos/', views.listar_pagos, name='listar_pagos'),
    path('pagos/crear/', views.crear_pago, name='crear_pago'),
    path('pagos/<int:pago_id>/', views.detalle_pago, name='detalle_pago'),

]

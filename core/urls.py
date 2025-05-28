from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('platos/crear/', views.crear_plato, name='crear_plato'),
    path('platos/<int:plato_id>/editar/', views.editar_plato, name='editar_plato'),
    path('platos/<int:plato_id>/eliminar/', views.eliminar_plato, name='eliminar_plato'),
]
]
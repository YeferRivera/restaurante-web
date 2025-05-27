from django.contrib import admin
from .models import Plato, Orden, Pago

admin.site.register(Plato)
admin.site.register(Orden)
admin.site.register(Pago)
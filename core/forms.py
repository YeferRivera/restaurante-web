from django import forms
from .models import Plato, Orden
from .models import Pago


class PlatoForm(forms.ModelForm):
    class Meta:
        model = Plato
        fields = ['nombre', 'descripcion', 'precio']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class OrdenForm(forms.ModelForm):
    class Meta:
        model = Orden
        fields = ['platos', 'pagada']
        widgets = {
            'platos': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
            'pagada': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class PagoForm(forms.ModelForm):
    class Meta:
        model = Pago
        fields = ['orden', 'monto']
        widgets = {
            'orden': forms.Select(attrs={'class': 'form-select'}),
            'monto': forms.NumberInput(attrs={'class': 'form-control'}),
        }

       
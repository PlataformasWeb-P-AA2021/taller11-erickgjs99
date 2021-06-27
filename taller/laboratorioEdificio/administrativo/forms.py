from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms

from administrativo.models import Edificio, \
    Departamento


class EdificioForm(ModelForm):
    class Meta:
        model = Edificio
        fields = ['nombre', 'direccion', 'ciudad', 'tipo']
        labels = {
            'nombre': _('Nombre del edificio'),
            'direccion': _('Dirección del edificio '),
            'ciudad': _('Ciudad del edificio '),
            'tipo': _('De que tipo es el edificio'),
        }

    def clean_ciudad(self):
        valor = self.cleaned_data['ciudad']
        if "L" in valor:
            raise forms.ValidationError("La ciudad no puede iniciar con L")
        return valor

    def clean_nombre(self):
        valor = self.cleaned_data['nombre']
        if "cuenca" in valor or "Cuenca" in valor or "CUENCA" in valor:
            raise forms.ValidationError("La ciudad de Cuenca no es válida")



class DepartamentoForm(ModelForm):
    class Meta:
        fields = ['nombreProp', 'costo', 'numCuartos', 'edificio']
        labels = {
            'nombreProp': _('Nombre del propietario del departamento'),
            'costo': _('Costo del departamento '),
            'numCuartos': _('Cuántos cuartos tiene el departamento'),
            'edificio': _('A que edificio pertenece el departamento'),
        }
    
    def clean_nombreProp(self):
        valor = self.cleaned_data['nombreProp']
        num_palabras = len(valor.split())
        if num_palabras > 3:
            raise forms.ValidationError("El nombre del propietario tiene que tener menos de tres palabras")
        return valor
    
    def clean_costo(self):
        valor = self.cleaned_data['costo']
        if valor > 100000:
            raise forms.ValidationError("El departamento no puede ser mayor a $100000")
        return valor

    def clean_numCuartos(self):
        valor = self.cleaned_data['numCuartos']
        if valor == 0:
           raise forms.ValidationError("El departamento tener ningún cuarto") 
        if valor > 7:
            raise forms.ValidationError("El departamento no puede tener más de 7 cuartos")
        return valor

class DepartamentoEdificioForm(ModelForm):

    def __init__(self, edificio, *args, **kwargs):
        super(DepartamentoEdificioForm, self).__init__(*args, **kwargs)
        self.initial['edificio'] = edificio
        self.fields["edificio"].widget = forms.widgets.HiddenInput()
  

    class Meta:
        model = Departamento
        fields = ['nombreProp', 'costo', 'numCuartos', 'edificio']
    
    def clean_nombreProp(self):
        valor = self.cleaned_data['nombreProp']
        num_palabras = len(valor.split())

        if num_palabras < 4:
            raise forms.ValidationError("Ingrese su nombre completo por favor")
        return valor


    def clean_numCuartos(self):
        valor = self.cleaned_data['numCuartos']
        if valor == 0 or valor > 7:
            raise forms.ValidationError("Ingrese un número de cuartos valido")
        return valor
        

    def clean_costo(self):
        valor = self.cleaned_data['costo']
        if (valor) > 100000:
            raise forms.ValidationError("Ingrese un costo valido")
        return valor



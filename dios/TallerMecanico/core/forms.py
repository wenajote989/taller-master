from django import forms
from .models import Contacto, Auto

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = '__all__'

class AutoForm(forms.ModelForm):

    class Meta:
        model = Auto
        fields = '__all__'
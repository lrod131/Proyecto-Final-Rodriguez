from django import forms
from .models import *

class ResponderComentario(forms.ModelForm):
    contenido = forms.CharField(label='Introduzca su comentario:')
    class Meta:
        model = Comentario
        fields = ['contenido']
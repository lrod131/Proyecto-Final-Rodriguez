from django import forms
from .models import *

class ResponderComentario(forms.ModelForm):
    contenido = forms.CharField(label='Introduzca su comentario:')
    class Meta:
        model = Comentario
        fields = ['contenido']

class PostForm(forms.ModelForm):
    destacado = forms.BooleanField(required=False, widget=forms.CheckboxInput)
    categorias = forms.ModelMultipleChoiceField(queryset=Categoria.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Post
        fields = ['titulo','subtitulo','slug','categorias','resumen','cuerpo','autor','destacado','imagen']


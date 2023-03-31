from .models import *

def procesador_categorias(request):
    categorias = Categoria.objects.all()
    return { 'lista_de_categorias':categorias}
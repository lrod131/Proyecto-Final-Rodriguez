from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views import generic

def home_page(request):
    post = Post.objects.all()
    categorias = Categoria.objects.all()
    destacado = Post.objects.filter(destacado=True)
    context = {'lista_de_posts':post, 'lista_de_categorias':categorias,'destacado':destacado}
    return render(request,'blogs/home.html',context=context)

class postDetailView(generic.DetailView):
    model = Post
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lista_de_categorias'] = Categoria.objects.all()
        return context


from django.shortcuts import render
from django.http import HttpResponse
from blogs.models import Post,Categoria
from django.views import generic
from django.utils import timezone
from django.db.models import Q


def home_page(request):
    post = Post.objects.filter(fecha_publicacion__lte=timezone.now())
    destacado = Post.objects.filter(destacado=True,fecha_publicacion__lte=timezone.now())
    context = {'lista_de_posts':post, 'destacado':destacado}
    return render(request,'blogs/home.html',context=context)

class postDetailView(generic.DetailView):
    model = Post
    queryset = Post.objects.filter(fecha_publicacion__lte=timezone.now())

class VistaPostDestacados(generic.ListView):
    model = Post
    template_name = 'blogs/lista_destacados.html'
    paginate_by = 1
    
    def get_queryset(self):
        query = Post.objects.filter(destacado=True,fecha_publicacion__lte=timezone.now())
        return query

class VistaListaCategorias(generic.ListView):
    model = Post
    template_name = 'blogs/lista_destacados.html'
    paginate_by = 1

    def get_queryset(self):
        query = self.request.path.replace('/categorias/','')
        post_list = Post.objects.filter(categorias__slug=query,fecha_publicacion__lte=timezone.now())
        return post_list

class VistaBuscar(generic.ListView):
    model = Post
    template_name = 'blogs/lista_destacados.html'
    paginate_by = 1

    def get_queryset(self):
        query = self.request.GET.get('search')
        resultados = Post.objects.filter(
            Q(titulo__icontains=query)|Q(categorias__titulo__icontains=query),fecha_publicacion__lte=timezone.now()).distinct()
        return resultados

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('search')
        return context
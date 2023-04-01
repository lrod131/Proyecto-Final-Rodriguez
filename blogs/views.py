from django.shortcuts import render
from django.views import generic,View
from django.views.generic.detail import SingleObjectMixin
from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.utils import timezone
from django.db.models import Q
from django.urls import reverse
from django.views.generic.edit import CreateView
from .models import *
from .forms import *

def about(request):
    return render(request,'blogs/about.html')

def home_page(request):
    post = Post.objects.filter(fecha_publicacion__lte=timezone.now())
    destacado = Post.objects.filter(destacado=True,fecha_publicacion__lte=timezone.now())
    context = {'lista_de_posts':post, 'destacado':destacado}
    return render(request,'blogs/home.html',context=context)

class postDetailView(generic.DetailView):
    model = Post
    queryset = Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['forms'] = ResponderComentario
        return context
    
class PostComentarioForm(LoginRequiredMixin, SingleObjectMixin, FormView):
    template_name = 'blogs/post_detail.html'
    form_class =  ResponderComentario
    model = Post
    
    def post(self,request,*args,**kwargs):
        self.object = self.get_object()
        return super().post(request,*args,**kwargs)
    
    def form_valid(self,form):
        f= form.save(commit=False)
        f.autor = self.request.user
        f.post= self.object
        f.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('blogs:post',kwargs={'slug':self.object.slug})+'#comments-section'

class PostCreate(CreateView):
    model = Post
    success_url ="/"
    form_class = PostForm

class PostView(View):
    def get(self,request,*args,**kwargs):
        view = postDetailView.as_view()
        return view(request,*args,**kwargs)
    
    def post(self,request,*args,**kargs):
        view = PostComentarioForm.as_view()
        return view(request,*args,**kargs)
    
class VistaPostDestacados(generic.ListView):
    model = Post
    template_name = 'blogs/lista_destacados.html'
    paginate_by = 10
    
    def get_queryset(self):
        query = Post.objects.filter(destacado=True,fecha_publicacion__lte=timezone.now())
        return query

class VistaListaCategorias(generic.ListView):
    model = Post
    template_name = 'blogs/lista_destacados.html'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.path.replace('/categorias/','')
        post_list = Post.objects.filter(categorias__slug=query,fecha_publicacion__lte=timezone.now())
        return post_list

class VistaBuscar(generic.ListView):
    model = Post
    template_name = 'blogs/lista_destacados.html'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('search')
        resultados = Post.objects.filter(
            Q(titulo__icontains=query)|Q(categorias__titulo__icontains=query),fecha_publicacion__lte=timezone.now()).distinct()
        return resultados

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('search')
        return context
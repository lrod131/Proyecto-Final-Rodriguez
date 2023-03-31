from django.urls import path
from . import views

app_name = 'blogs'
urlpatterns = [
    path('',views.home_page),
    path('post/<slug:slug>',views.postDetailView.as_view(),name='post'),
    path('destacados/',views.VistaPostDestacados.as_view(),name='destacados'),
    path('categorias/<slug:slug>',views.VistaListaCategorias.as_view(),name='listaCategorias'),
    path('buscar/',views.VistaBuscar.as_view(),name='buscar')
]
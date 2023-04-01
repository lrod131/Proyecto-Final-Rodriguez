from django.urls import path
from . import views

app_name = 'blogs'
urlpatterns = [
    path('',views.home_page,name='home'),
    path('page/<slug:slug>',views.PostView.as_view(),name='post'),
    path('createPage/',views.PostCreate.as_view(),name='create'),
    path('destacados/',views.VistaPostDestacados.as_view(),name='destacados'),
    path('categorias/<slug:slug>',views.VistaListaCategorias.as_view(),name='listaCategorias'),
    path('buscar/',views.VistaBuscar.as_view(),name='buscar'),
    path('about/',views.about,name='acerca'),
]
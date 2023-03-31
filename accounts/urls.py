from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name='accounts'

urlpatterns =[
    path('registro/',views.registro_usuario.as_view(),name='Registro'),
    path('success/', TemplateView.as_view(template_name='accounts/success_registration.html'),name='Success')    
]
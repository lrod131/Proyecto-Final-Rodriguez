
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import *

class registro_usuario(FormView):
    template_name= 'accounts/registro.html'
    form_class = FormularioRegistro
    success_url = reverse_lazy('accounts:Success')
    
    def form_valid(self, form):
        form.save()
        return super(registro_usuario, self).form_valid(form)
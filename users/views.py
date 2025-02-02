from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import User
from .forms import RegisterForm
import base64
from django.core.files.base import ContentFile
# Create your views here.


class UserRegistrationView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('success')

    def post(self, request, *args, **kwargs):
        form = self.get_form()

        if form.is_valid(): 
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
        
    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)
    

def final(request):
    return render(request=request,template_name='final.html')
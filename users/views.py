from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView
from .forms import Rform


class RegisterView(CreateView):
    template_name = 'users/register.html'
    form_class = Rform
    success_url = '/'

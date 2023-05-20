from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView,ListView,DetailView,CreateView
from app.models import *

class home(TemplateView):
    template_name='app/home.html'

class List_of_school(ListView):
    model=School
    context_object_name='schools'

class school_details(DetailView):
    model=School
    context_object_name='schools'

class Create_school(CreateView):
    model=School
    fields='__all__'
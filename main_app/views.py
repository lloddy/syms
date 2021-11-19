from django.shortcuts import render
from .models import Sym, syms

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def syms_index(request):
    return render(request, 'syms/index.html', { 'syms': syms })
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Sym

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def syms_index(request):
    syms = Sym.objects.all()
    return render(request, 'syms/index.html', { 'syms': syms })

def syms_detail(request, sym_id):
    sym = Sym.objects.get(id=sym_id)
    return render(request, 'syms/detail.html', { 'sym': sym })

class SymCreate(CreateView):
    model = Sym
    fields = '__all__'

class SymUpdate(UpdateView):
    model = Sym
    fields = ['gender', 'occupation', 'description']

class SymDelete(DeleteView):
    model = Sym
    success_url = '/syms/'
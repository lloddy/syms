from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Sym
from .forms import FeedingForm

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
    feeding_form = FeedingForm()
    return render(request, 'syms/detail.html', {
        'sym': sym,
        'feeding_form': feeding_form
        })

def add_feeding(request, sym_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.sym_id = sym_id
        new_feeding.save()
    return redirect('detail', sym_id=sym_id)

class SymCreate(CreateView):
    model = Sym
    fields = '__all__'

class SymUpdate(UpdateView):
    model = Sym
    fields = ['gender', 'occupation', 'description']

class SymDelete(DeleteView):
    model = Sym
    success_url = '/syms/'
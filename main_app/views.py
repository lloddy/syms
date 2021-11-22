from django.core.exceptions import TooManyFieldsSent
from django.db.models import fields
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
import uuid
import boto3
from .models import Sym, Affliction, Photo
from .forms import FeedingForm

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'cat-collector-image-bucket'

# Create your views here.

def add_photo(request, sym_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.')]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f'{S3_BASE_URL}{BUCKET}/{key}'
            photo = Photo(url=url, sym_id=sym_id)
            photo.save()
        except:
            print('An error occured uploading file to s3')
    return redirect('detail', sym_id=sym_id)

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def syms_index(request):
    syms = Sym.objects.all()
    return render(request, 'syms/index.html', { 'syms': syms })

def syms_detail(request, sym_id):
    sym = Sym.objects.get(id=sym_id)
    afflictions_sym_doesnt_have = Affliction.objects.exclude(id__in = sym.afflictions.all().values_list('id'))
    feeding_form = FeedingForm()
    return render(request, 'syms/detail.html', {
        'sym': sym,
        'feeding_form': feeding_form,
        'afflictions': afflictions_sym_doesnt_have
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

class AfflictionList(ListView):
    model = Affliction

class AfflictionDetail(DetailView):
    model = Affliction

class AfflictionCreate(CreateView):
    model = Affliction
    fields = '__all__'

class AfflictionUpdate(UpdateView):
    model = Affliction
    fields = '__all__'

class AfflictionDelete(DeleteView):
    model = Affliction
    success_url = '/afflictions'

def assoc_affliction(request, sym_id, affliction_id):
    Sym.objects.get(id=sym_id).afflictions.add(affliction_id)
    return redirect('detail', sym_id=sym_id)
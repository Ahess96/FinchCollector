from django.shortcuts import render, redirect
from .models import Finch, Land
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import FeedingForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', {
        'finches': finches
    })

def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    #instantiate Feedingform to be rendered
    id_list = finch.lands.all().values_list('id')
    lands_finch_doesnt_have = Land.objects.exclude(id__in=id_list)
    feeding_form = FeedingForm()
    return render(request, 'finches/detail.html', { 'finch': finch, 'feeding_form': feeding_form, 'lands': lands_finch_doesnt_have })

class FinchCreate(CreateView):
    model = Finch
    fields = ['name', 'breed', 'description']

class FinchUpdate(UpdateView):
    model = Finch
    fields = '__all__'

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches'

def add_feeding(request, finch_id):
  # create a ModelForm instance using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.finch_id = finch_id
    new_feeding.save()
  return redirect('detail', finch_id=finch_id)

def assoc_land(request, finch_id, land_id):
    Finch.objects.get(id=finch_id).lands.add(land_id)
    return redirect('detail', finch_id=finch_id)

def unassoc_land(request, finch_id, land_id):
    Finch.objects.get(id=finch_id).lands.remove(land_id)
    return redirect('detail', finch_id=finch_id)

class LandList(ListView):
    model = Land

class LandDetail(DetailView):
    model = Land

class LandCreate(CreateView):
    model = Land
    fields = '__all__'

class LandUpdate(UpdateView):
    model = Land
    fields = ['location', 'climate']

class LandDelete(DeleteView):
    model = Land
    success_url = '/lands'

from django.shortcuts import render
from .models import Finch

# finches = [
#     {"breed": "Zebra Finch", "name": "Eric", "description": "Small, social finch with distinct black and white striped markings."},
#     {"breed": "Gouldian Finch", "name": "Vilem", "description": "Colorful, social finch with bright red, green, and blue markings."},
#     {"breed": "Society Finch", "name": "Kendall", "description": "Easy to care for, social finch with a variety of color mutations."},
#     {"breed": "Goldfinch", "name": "Anthony", "description": "Small, songbird with bright yellow plumage and distinctive song."},
#     {"breed": "European Greenfinch", "Justin": "Ernie", "description": "Medium-sized finch with olive-green plumage and a melodious song."}
# ]


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
    return render(request, 'finches/detail.html', { 'finch': finch })

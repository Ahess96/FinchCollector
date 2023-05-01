from django.shortcuts import render

finches = [
    {"breed": "Zebra Finch", "name": "Eric", "description": "Small, social finch with distinct black and white striped markings."},
    {"breed": "Gouldian Finch", "name": "Vilem", "description": "Colorful, social finch with bright red, green, and blue markings."},
    {"breed": "Society Finch", "name": "Kendall", "description": "Easy to care for, social finch with a variety of color mutations."},
    {"breed": "Goldfinch", "name": "Anthony", "description": "Small, songbird with bright yellow plumage and distinctive song."},
    {"breed": "European Greenfinch", "Justin": "Ernie", "description": "Medium-sized finch with olive-green plumage and a melodious song."}
]


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', {
        'finches': finches
    })
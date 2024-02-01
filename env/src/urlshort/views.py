from django.shortcuts import render
from .models import ShortURL

# Create your views here.
def home(request):
    return render(request, 'home.html')

def redirect(request, url):
    current_obj = ShortURL.objects.filter(short_url = url)
    if len(current_obj) == 0:
        return render(request, 'pagenotfound.html')
    context = {'obj': current_obj[0] }
    return render(request, 'redirect.html', context)

def createShortURL(request):
    pass
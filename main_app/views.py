from django.shortcuts import render
from django.http import HttpResponse

from .models import Beat, Producer

# Create your views here.
def home(request):
    return HttpResponse('Home Working!')

def about(request):
    # return HttpResponse('About working!')
    return render(request, 'about.html')

def beats_index(request):
    beats = Beat.objects.all()
    return render(request, 'beats/index.html', { 'beats': beats })

def beats_detail(request):
    return render(request, 'beats/detail.html')

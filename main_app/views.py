from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Beat, Producer

# Create your views here.
def home(request):
    # return HttpResponse('Home Working!')
    return render(request, 'home.html')

def about(request):
    # return HttpResponse('About working!')
    return render(request, 'about.html')

def beats_index(request):
    beats = Beat.objects.all()
    return render(request, 'beats/index.html', { 'beats': beats })

def beats_detail(request, beat_id):
    beat = Beat.objects.get(id=beat_id)
    return render(request, 'beats/detail.html', { 'beat': beat})

class BeatCreate(CreateView):
    model = Beat
    # fields = '__all__'
    fields = ['name', 'genre', 'url']
    # success_url = '/beats/'

    # method is called when a form has been POSTed
    # should return a http response; default returns to 'success_url' or in this case 'get_absolute_url' in 'models.py'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class BeatUpdate(UpdateView):
    model = Beat
    fields = ['name', 'genre']

class BeatDelete(DeleteView):
    model = Beat
    success_url = '/beats/'
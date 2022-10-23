from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

import uuid
import boto3
from .models import Beat, Producer

S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'beatstore-titans'

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

    # producers a beat doesn't have
    uncredited_producers = Producer.objects.exclude(id__in = beat.producers.all().values_list('id'))
    return render(request, 'beats/detail.html', { 'beat': beat, 'producers': uncredited_producers })

# def add_audio(request, beat_id):
#     # photo-file will be the "name" attribute on the <input type="file">
#     audio_file = request.FILES.get('audio-file', None)
#     if audio_file:
#         s3 = boto3.client('s3')
#         # need a unique "key" for S3 / needs image file extension too
#         key = uuid.uuid4().hex[:6] + audio_file.name[audio_file.name.rfind('.'):]
#         # just in case something goes wrong
#         try:
#             s3.upload_fileobj(audio_file, BUCKET, key)
#             # build the full url string
#             url = f"{S3_BASE_URL}{BUCKET}/{key}"
#             # we can assign to cat_id or cat (if you have a cat object)
#             audio = Audio(url=url, beat_id=beat_id)
#             audio.save()
#         except:
#             print('An error occurred uploading file to S3')
#     return redirect('beats_detail', beat_id=beat_id)

def assoc_producer(request, beat_id, producer_id):
    Beat.objects.get(id=beat_id).producers.add(producer_id)
    return redirect('beats_detail', beat_id=beat_id)

class BeatCreate(CreateView):
    model = Beat
    # fields = '__all__'
    fields = ['name', 'genre', 'bpm', 'key', 'image', 'audio']
    # success_url = '/beats/'

    # method is called when a form has been POSTed
    # should return a http response; default returns to 'success_url' or in this case 'get_absolute_url' in 'models.py'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class BeatUpdate(UpdateView):
    model = Beat
    fields = ['name', 'genre', 'bpm', 'key', 'image', 'audio']

class BeatDelete(DeleteView):
    model = Beat
    success_url = '/beats/'

class ProducerList(ListView):
    model = Producer
    template_name = 'producers/index.html'

class ProducerCreate(CreateView):
    model = Producer
    fields = ['name', 'IG', 'twitter', 'tiktok']

class ProducerDetail(DetailView):
    model = Producer
    template_name = 'producers/detail.html'

class ProducerUpdate(UpdateView):
    model = Producer
    fields = ['name', 'IG', 'twitter', 'tiktok']

class ProducerDelete(DeleteView):
    model = Producer
    success_url = '/producers/'
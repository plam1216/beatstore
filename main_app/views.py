from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User

# logs in user (GET request)
from django.contrib.auth import login

# creates user (POST request)
from django.contrib.auth.forms import UserCreationForm

# authorization for functions
from django.contrib.auth.decorators import login_required

# authorization for CBV
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Beat, Producer
from .forms import CommentForm

S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'beatstore-titans'

# Create your views here.
def home(request):
    # return HttpResponse('Home Working!')
    return render(request, 'home.html')

def about(request):
    # return HttpResponse('About working!')
    return render(request, 'about.html')

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('beats_index')
        else:
            error_message = 'Invalid sign up - try again'
    
    # A bad GET or POST request so page will rerender 'signup.html' with empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

def beats_index(request):
    beats = Beat.objects.all()
    awsurl = f"{S3_BASE_URL}{BUCKET}"
    return render(request, 'beats/index.html', { 'beats': beats, 'awsurl': awsurl })

def beats_detail(request, beat_id):
    beat = Beat.objects.get(id=beat_id)
    awsurl = f"{S3_BASE_URL}{BUCKET}"

    # instantiate comment form
    comment_form = CommentForm()

    # get producers a beat doesn't have
    uncredited_producers = Producer.objects.exclude(id__in = beat.producers.all().values_list('id'))
    return render(request, 'beats/detail.html', { 'beat': beat, 'producers': uncredited_producers, 'comment_form': comment_form, 'awsurl': awsurl })

def producers_index(request):
    producers = Producer.objects.all()
    return render(request, 'producers/index.html', { 'producers': producers })

def producers_detail(request, producer_id):
    producer = Producer.objects.get(id=producer_id)
    producer_beats = producer.beat_set.all()
    awsurl = f"{S3_BASE_URL}{BUCKET}"

    return render(request, 'producers/detail.html', {'producer': producer, 'producer_beats': producer_beats, 'awsurl': awsurl})

@login_required
def my_beats(request):
    curr_user = User.objects.get(id=request.user.id)
    curr_user_beats = curr_user.beat_set.all()
    awsurl = f"{S3_BASE_URL}{BUCKET}"
    return render(request, 'my_beats.html', {'curr_user_beats': curr_user_beats, 'awsurl': awsurl})

@login_required
def assoc_producer(request, beat_id, producer_id):
    Beat.objects.get(id=beat_id).producers.add(producer_id)
    return redirect('beats_detail', beat_id=beat_id)

@login_required
def unassoc_producer(request, beat_id, producer_id):
    Beat.objects.get(id=beat_id).producers.remove(producer_id)
    return redirect('beats_detail', beat_id=beat_id)

@login_required
def add_comment(request, beat_id):
    # curr_user = request.user
    form = CommentForm(request.POST)
    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.beat_id = beat_id
        new_comment.save()
    # return redirect('beats_detail', beat_id=beat_id, curr_user=curr_user)
    return redirect('beats_detail', beat_id=beat_id)

class BeatCreate(LoginRequiredMixin, CreateView):
    model = Beat
    # fields = '__all__'
    fields = ['name', 'genre', 'bpm', 'key', 'image', 'audio']
    # success_url = '/beats/'

    # method is called when a form has been POSTed
    # should return a http response; default returns to 'success_url' or in this case 'get_absolute_url' in 'models.py'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class BeatUpdate(LoginRequiredMixin, UpdateView):
    model = Beat
    fields = ['name', 'genre', 'bpm', 'key', 'image', 'audio']

class BeatDelete(LoginRequiredMixin, DeleteView):
    model = Beat
    success_url = '/beats/'

class ProducerCreate(LoginRequiredMixin, CreateView):
    model = Producer
    fields = ['name', 'IG', 'twitter', 'tiktok']

class ProducerUpdate(LoginRequiredMixin, UpdateView):
    model = Producer
    fields = ['name', 'IG', 'twitter', 'tiktok']

class ProducerDelete(LoginRequiredMixin, DeleteView):
    model = Producer
    success_url = '/producers/'
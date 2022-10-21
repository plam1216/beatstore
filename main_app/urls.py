from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('beats/', views.beats_index, name='beats_index'),
    path('beats/detail', views.beats_detail, name='beats_detail'),
]
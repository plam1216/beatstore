from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('beats/', views.beats_index, name='beats_index'),
    path('beats/<int:beat_id>', views.beats_detail, name='beats_detail'),
    path('beats/create/', views.BeatCreate.as_view(), name='beats_create'),
    path('beats/<int:pk>/update/', views.BeatUpdate.as_view(), name='beats_update'),
    path('beats/<int:pk>/delete/', views.BeatDelete.as_view(), name='beats_delete'),
]
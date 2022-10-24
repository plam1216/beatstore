from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('my_beats/', views.my_beats, name='my_beats'),
    path('beats/', views.beats_index, name='beats_index'),
    path('beats/<int:beat_id>', views.beats_detail, name='beats_detail'),
    path('producers/<int:producer_id>/', views.producers_detail, name='producers_detail'),
    
    # add comment to a Beat (M:1)
    path('beats/<int:beat_id>/add_comment/', views.add_comment, name='add_comment'),

    # associate Producer w/ Beat (M:M)
    path('beats/<int:beat_id>/assoc_producer/<int:producer_id>/', views.assoc_producer, name='assoc_producer'),
    path('beats/<int:beat_id>/unassoc_producer/<int:producer_id>/', views.unassoc_producer, name='unassoc_producer'),

    # Beat CBV
    path('beats/create/', views.BeatCreate.as_view(), name='beats_create'),
    path('beats/<int:pk>/update/', views.BeatUpdate.as_view(), name='beats_update'),
    path('beats/<int:pk>/delete/', views.BeatDelete.as_view(), name='beats_delete'),

    # Producer CBV
    path('producers/', views.ProducerList.as_view(), name='producers_index'),
    path('producers/create/', views.ProducerCreate.as_view(), name='producers_create'),
    # path('producers/<int:pk>/', views.ProducerDetail.as_view(), name='producers_detail'),
    path('producers/<int:pk>/update/', views.ProducerUpdate.as_view(), name='producers_update'),
    path('producers/<int:pk>/delete/', views.ProducerDelete.as_view(), name='producers_delete'),
    # Sign Up
    path('accounts/signup/', views.signup, name='signup'),
]
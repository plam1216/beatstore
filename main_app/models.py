from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
LEASES = (
    ('Premium', 'Premium'),
    ('Unlimited', 'Unlimited'),
    ('Exclusive', 'Exclusive'),
)

class Producer(models.Model):
    name = models.CharField(max_length=50)
    IG = models.CharField(max_length=50)
    twitter = models.CharField(max_length=50)
    tiktok = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.name}, IG: {self.IG}, Twitter: {self.twitter}, TikTok: {self.tiktok}'

    def get_absolute_url(self):
        return reverse('producers_detail', kwargs={'producer_id':self.id})

class Beat(models.Model):
    name = models.CharField(max_length=200)
    genre = models.CharField(max_length=50)
    bpm = models.IntegerField()
    key = models.CharField(max_length=50)
    image = models.FileField()
    audio = models.FileField()

    # M:M relationship (Many Producers : Many Beats)
    producers = models.ManyToManyField(Producer)

    # 1:M relationship (1 User : Many Beats)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, Genre: {self.genre}, BPM: {self.bpm}, Key: {self.key}'

    def get_absolute_url(self):
        return reverse('beats_detail', kwargs={'beat_id': self.id})

class Comment(models.Model):
    message = models.CharField(max_length=200)

    beat = models.ForeignKey(Beat, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.message}'
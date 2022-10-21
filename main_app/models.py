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
    name = models.CharField(max_length=20)
    ig = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.name} @{self.ig}'

class Beat(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=20)
    url = models.CharField(max_length=200)

    # M:M relationship (Many Producers : Many Beats)
    # producers = models.ManyToManyField(Producer)

    # 1:M relationship (1 User : Many Beats)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # def __str__(self):
        # return f'{self.name}; Produced by: ${self.producers}'

    def get_absolute_url(self):
        return reverse('beats_detail', kwargs={'beat_id': self.id})
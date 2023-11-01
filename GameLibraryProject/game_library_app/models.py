from django.db import models
from django.urls import reverse # Needed for def get_absolute_url

# Create your models here.
class SiteUser(models.Model):

    PRIMARY_GAME_PLATFORM = [
        ('PC', 'Steam'),
        ('PC', 'Epic Games'),
        ('PC', 'Battle.net'),
        ('PC', 'GOG'),
        ('Console', 'Playstation'),
        ('Console', 'Xbox'),
        ('Console', 'Nintendo'),
        ('Mobile', 'Android'),
        ('Mobile', 'iOS'),
    ]

    # Attributes
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    platform = models.CharField(max_length=50, choices=PRIMARY_GAME_PLATFORM)


    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('user_detail', args=[str(self.id)])
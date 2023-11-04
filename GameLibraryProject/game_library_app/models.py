from django.db import models
from django.urls import reverse # Needed for def get_absolute_url

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
        ('Any', 'Any Platform'),
    ]

GAME_GENRE = [
        ('Action', 'Action'),
        ('Adventure', 'Adventure'),
        ('RPG', 'RPG'),
        ('Strategy', 'Strategy'),
        ('Simulation', 'Simulation'),
        ('Sports', 'Sports'),
        ('Puzzle', 'Puzzle'),
        ('Idle', 'Idle'),
        ('Other', 'Other'),
    ]


# Create your models here.
class SiteUser(models.Model):

    # Attributes
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    platform = models.CharField(max_length=50, choices=PRIMARY_GAME_PLATFORM)


    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('user_detail', args=[str(self.id)])
    
    
class GameLibrary(models.Model):

    # Attributes
    user = models.ForeignKey(SiteUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    platform = models.CharField(max_length=50, choices=PRIMARY_GAME_PLATFORM, default='Any')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('game_library_detail', args=[str(self.id)])
    

class GameInLibrary(models.Model):

    # Attributes
    title = models.CharField(max_length=50)
    genre = models.CharField(max_length=50, choices=GAME_GENRE, default='Other')
    platform = models.CharField(max_length=50, choices=PRIMARY_GAME_PLATFORM)
    library = models.ForeignKey(GameLibrary, on_delete=models.CASCADE)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('game_detail', args=[str(self.id)])
    


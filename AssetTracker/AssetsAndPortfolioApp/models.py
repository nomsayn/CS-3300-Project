from django.db import models
from django.urls import reverse



# perhaps add public/private portfolios
class WebSiteUser(models.Model):

    EXPERIENCE = (
        ('Beginner', '0 - 2 years'),
        ('Advanced', '2 - 5 years'),
        ('Expert', '5+ years'),
    )

    # Attributes
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    financial_experience = models.CharField(max_length=50, choices=EXPERIENCE)


    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('user_detail', args=[str(self.id)])
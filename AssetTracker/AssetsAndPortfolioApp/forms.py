from django.forms import ModelForm
from .models import WebSiteUser

class UserForm(ModelForm):
    class Meta:
        model = WebSiteUser
        fields = ['name', 'email', 'financial_experience']
from django.forms import ModelForm
from .models import SiteUser


class UserForm(ModelForm):
    class Meta:
        model = SiteUser
        fields = ['name', 'email', 'platform']
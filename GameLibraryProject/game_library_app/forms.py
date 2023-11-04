from django.forms import ModelForm
from .models import SiteUser, GameLibrary


class UserForm(ModelForm):
    class Meta:
        model = SiteUser
        fields = ['name', 'email', 'platform']


# class NewGameLibraryForm(ModelForm):
#     class Meta:
#         model = GameLibrary
#         fields = ['title']
from django.contrib import admin
from .models import SiteUser, GameLibrary, GameInLibrary

# Register your models here.
admin.site.register(SiteUser)
admin.site.register(GameLibrary)
admin.site.register(GameInLibrary)
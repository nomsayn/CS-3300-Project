from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic
from .forms import UserForm
from .models import WebSiteUser

# Create your views here.
def index(request):
    return render(request, 'AssetsAndPortfolioApp/index.html')

def create_user(request):
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            print('form is valid')
            # save form information as new WebSiteUser object to database
            form.save()

            return render(request, 'AssetsAndPortfolioApp/index.html')
        
    context = {'form': form}
    return render(request, 'AssetsAndPortfolioApp/create_user.html', context)
            

class UserListView(generic.ListView):
    model = WebSiteUser
    template_name = 'AssetsAndPortfolioApp/user_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_list'] = WebSiteUser.objects.all()
        return context

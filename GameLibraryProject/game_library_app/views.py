from django.shortcuts import render
from .models import SiteUser
from .forms import UserForm
from django.views import generic

# Create your views here.
def index (request):
    return render(request, 'game_library_app/index.html')


def create_user(request):
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            print('form is valid')
            # save form information as new WebSiteUser object to database
            form.save()

            return render(request, 'game_library_app/index.html')
        
    context = {'form': form}
    return render(request, 'game_library_app/create_user.html', context)


class UserListView(generic.ListView):
    model = SiteUser
    template_name = 'game_library_app/user_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_list'] = SiteUser.objects.all()
        return context

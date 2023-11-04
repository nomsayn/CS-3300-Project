from django.shortcuts import render
from .models import SiteUser, GameLibrary
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
    
class UserDetailView(generic.DetailView):
    model = SiteUser
    template_name = 'game_library_app/user_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = SiteUser.objects.all().filter(id=self.kwargs['pk'])
        context['game_libraries'] = context['user'][0].gamelibrary_set.all().order_by('title')
        print(context['user'])
        print(context['game_libraries'])
        return context
    
class GameLibraryDetailView(generic.DetailView):
    model = GameLibrary
    template_name = 'game_library_app/game_library_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['game_library'] = GameLibrary.objects.all().filter(id=self.kwargs['pk'])
        context['games'] = context['game_library'][0].gameinlibrary_set.all().order_by('title')
        print(context['game_library'])
        # print(context['games'])
        return context
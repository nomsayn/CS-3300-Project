from django.shortcuts import render, redirect
from .models import SiteUser, GameLibrary
from .forms import UserForm, NewGameLibraryForm, AddGameToLibraryForm
from django.views import generic

# Create your views here.
def index (request):
    print('index view')
    print(request)
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

def Create_Game_Library(request, pk):
    form = NewGameLibraryForm()
    user_id = pk

    if request.method == 'POST':
        form = NewGameLibraryForm(request.POST)

        if form.is_valid():
            new_library = form.save(commit=False)
            new_library.user = SiteUser.objects.get(id=user_id)
            print('form is valid')
            
            new_library.save()
            return redirect('user_detail', pk=user_id)

    context = {'form': form}
    return render(request, 'game_library_app/create_game_library.html', context)

def Add_Game_To_Library(request, pk):
    form = AddGameToLibraryForm()
    library_id = pk

    if request.method == 'POST':
        form = AddGameToLibraryForm(request.POST)

        if form.is_valid():
            new_game = form.save(commit=False)
            new_game.library = GameLibrary.objects.get(id=library_id)
            print('form is valid')
            
            new_game.save()
            return redirect('game_library_detail', pk=library_id)

    context = {'form': form}
    return render(request, 'game_library_app/add_game_to_library.html', context)



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
        context['game_libraries'] = context['user'][0].gamelibrary_set.all()
        # Alphabetic, ignore case, game library sorting
        context['game_libraries'] = sorted(context['game_libraries'], key=lambda x: x.title.lower())
        return context
    
class GameLibraryDetailView(generic.DetailView):
    model = GameLibrary
    template_name = 'game_library_app/game_library_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['game_library'] = GameLibrary.objects.all().filter(id=self.kwargs['pk'])
        context['games'] = context['game_library'][0].gameinlibrary_set.all().order_by('title')
        context['game_library_id'] = self.kwargs['pk']
        print(context['game_library'])
        # print(context['games'])
        return context
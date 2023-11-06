from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_user/', views.create_user, name='create_user'),
    path('user_detail/<int:pk>/create_game_library/', views.Create_Game_Library, name='create_game_library'),
    path('game_library_detail/<int:pk>/add_game_to_library/', views.Add_Game_To_Library, name='add_game_to_library'),
    path('user_list/', views.UserListView.as_view(), name='user_list'),
    path('user_detail/<int:pk>', views.UserDetailView.as_view(), name='user_detail'),
    path('game_library_detail/<int:pk>', views.GameLibraryDetailView.as_view(), name='game_library_detail'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_user/', views.create_user, name='create_user'),
    path('user_list/', views.UserListView.as_view(), name='user_list'),
    path('user_detail/<int:pk>', views.UserDetailView.as_view(), name='user_detail'),
    path('game_library_detail/<int:pk>', views.GameLibraryDetailView.as_view(), name='game_library_detail'),
]
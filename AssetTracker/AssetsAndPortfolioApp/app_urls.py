from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_user/', views.create_user, name='create_user'),
    path('user_list/', views.UserListView.as_view(), name='user_list'),
]
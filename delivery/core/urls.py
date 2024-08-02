from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('', views.index, name="index"),
    path('user-add/', views.user_add, name="user-add"),
    path('users-page/', views.users_page, name="users-page")
]

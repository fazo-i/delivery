from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, get_user_model

from .models import DocPack, User

from .forms import UserForm

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = get_user_model().objects.get(username=username)
        except:
            pass
        # Функция аутентификации
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('users')
    context = {}
    return render(request, 'login.html', context)

def index(request):
    docpacks = DocPack.objects.all()
    context = {'docpacks': docpacks}
    return render(request, 'index.html', context)

def user_add(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
    
    context = {'form': form} 
    return render(request, 'users/user-add.html', context)

def users_page(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'users/users-page.html', context)

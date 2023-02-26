from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth




def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return render(request, 'user/register_done.html', {'new_user': new_user})
    else:
        form = UserRegisterForm()


    return render(request, 'user/register.html', {'form': form})


def login_v(request):
    if request.method == 'POST':
        # username = request.POST["username"]
        # password = request.POST["password"]
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect('mybooks:profile')
    else:
        form = AuthenticationForm()
    return render(request, 'user/login.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')

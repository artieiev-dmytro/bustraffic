from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate

from .forms import LoginForm


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user.is_active and user:
                login(request, user)
                return redirect('routes:home')
    else:
        form = LoginForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('routes:home')

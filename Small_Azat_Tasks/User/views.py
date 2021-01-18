from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created!. Now able to log in')
            return redirect('login_url')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', context={'form': form})

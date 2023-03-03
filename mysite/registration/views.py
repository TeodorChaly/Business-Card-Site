from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import RegistrationForm

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main_page')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'registration/login.html')

def user_logout(request):
    logout(request)
    return render(request, 'registration/logout.html')

def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully. Please log in.')
            return redirect('login')
    else:
        form = RegistrationForm()

    return render(request, 'registration/registration.html', {'form': form})


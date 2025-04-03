from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import LoginForm, RegistrationForm

# Create your views here.
def login_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
        else:
            return redirect('login_user')

    form = LoginForm()
    context = {
        'form_type': 'Login',
        'form': form
    }
    return render(request, 'register.html', context=context)


def register_user(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('home')

    form = RegistrationForm()
    context = {
        'form_type': "Register",
        'form': form
    }
    return render(request, 'register.html', context=context)


def logout_user(request):
    logout(request)
    return redirect('login_user')

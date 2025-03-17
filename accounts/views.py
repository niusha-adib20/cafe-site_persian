from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from .forms import LoginForm
from django.contrib.auth import logout




def home(request):
    return render(request, 'home.html')

def menu(request):
    return render(request, 'menu.html')  



def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('home')  
        else:
            messages.error(request, "⛔ نام کاربری یا رمز عبور اشتباه است!")
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User(username=form.cleaned_data['username'], email=form.cleaned_data['email'])
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, ".ثبت‌ نام موفق! حالا می‌توانید وارد شوید")
            return redirect('register')  
        else:
            
            for field, errors in form.errors.items():
                for error in errors:
                    if field == 'password_confirm':
                        messages.error(request, f"!تأیید رمز عبور: {error}")
                    elif field == 'email':
                        messages.error(request, f"!ایمیل: {error}")
                    else:
                        messages.error(request, f"{form.fields[field].label}: {error}")
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})

def reservation(request):
    return render(request, 'reservation.html')

def user_logout(request):
    logout(request)
    return redirect('home')



from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.hashers import make_password
from .models import CustomUser


def signup(request):
    error = None
    
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password1']
        password2 = request.POST['password2']

        if password != password2:
            error = "Passwords do not match"
        elif CustomUser.objects.filter(email=email).exists():
            error = "Email is already registered"
        else:
            user = CustomUser.objects.create(
                name=name,
                email=email,
                password=make_password(password),
            )
            # Re-authenticate the user and specify the backend manually
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect('pages:index')

    return render(request, 'account/signup.html', {'error': error})


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('pages:index')
        else:
            # In case of a failed login attempt
            return render(request, 'account/login.html', {'error': 'Invalid login credentials'})
    else:
        return render(request, 'account/login.html')
    
    
def logout_view(request):
    logout(request)
    return redirect('pages:index') 
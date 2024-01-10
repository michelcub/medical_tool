from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password


from .models import Doctor



# Create your views here.
def login_view(request):
    return render(request, 'auth/login.html')

def register_view(request):
    return render(request, 'auth/register.html')

def recovery_view(request):
    return render(request, 'auth/recovery.html')

def activation_view(request):
    return render(request, 'auth/activation.html')


def register(request):
    user = None
    if request.method == 'POST':
        name = request.POST.get('name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        hashed_password = make_password(password)
        
        user = Doctor(email=email, password=hashed_password, name=name, last_name=last_name)
        user.save()
    
    if user:
        login(request, user)
        return redirect('auth:login')
    
    
def login(request):
    user = None
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = Doctor.objects.get(email=email)
        
        if user.check_password(password):
            login(request, user)
            return redirect('auth:login')
        else:
            return redirect('auth:login')
    
    if user:
        login(request, user)
        return redirect('auth:login')
    
    return redirect('auth:login')
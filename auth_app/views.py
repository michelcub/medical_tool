from django.contrib.auth import login as django_login
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password


from .models import Employee



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
        
        user = Employee(email=email, password=hashed_password, name=name, last_name=last_name)
        user.save()
    
    if user:
        django_login(request)
        return redirect('auth:login')
    
    
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = Employee.objects.filter(email=email).last()
        
        if user and user.check_password(password):
            django_login(request, user)
            print('Usuario válido')
            return redirect('app:settings_view')
        elif user:
            # Usuario válido pero contraseña incorrecta
            print('Contraseña incorrecta')
            return redirect('auth:login')
        else:
            # Usuario no encontrado, redirigir al registro
            print('Usuario no encontrado')
            return redirect('auth:register')
    
    return render(request, 'login.html') 
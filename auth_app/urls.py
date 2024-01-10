from django.urls import path

from . import views

app_name = 'auth'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('recovery/', views.recovery_view, name='recovery'),
    path('activation/', views.activation_view, name='activation'),
    
    # API
    path('api/register/', views.register, name='api_register'),
    path('api/login/', views.login, name='api_login'),
]



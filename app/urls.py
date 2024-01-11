from django.urls import path, include

from . import views

app_name = "app"

urlpatterns = [
    path("settings/", views.settings_view, name="settings_view"),
    path("paciente/", include("paciente.urls")),
]

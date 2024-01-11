from django.urls import path

from . import views

urlpatterns = [
    path("", views.paciente_view, name="paciente_view"),
    path("<int:paciente_id>", views.paciente_file, name="paciente_file"),
    path("new/", views.paciente_new, name="paciente_new"),
]
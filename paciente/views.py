from django.shortcuts import render

from .models import Paciente


# Create your views here.
def paciente_view(request):
    return render(request, "app/paciente/paciente_view.html")

def paciente_file(request, paciente_id):
    if request.method == "POST":
        paciente = Paciente.objects.filter(id=paciente_id).first()
    return render(request, "app/paciente/paciente_file.html", {"paciente": paciente})

def paciente_new(request):
    return render(request, "app/paciente/paciente_new.html")


def paciente(request):
    return render(request, "app/paciente/paciente.html")
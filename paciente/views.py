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
    if request.method == "POST":
        paciente = Paciente()
        paciente.nombre = request.POST.get("nombre")
        paciente.apellidos = request.POST.get("apellidos")
        paciente.fecha_nacimiento = request.POST.get("fecha_nacimiento")
        paciente.tipo_documento = request.POST.get("tipo_documento")
        paciente.documento_identidad = request.POST.get("documento_identidad")
        paciente.tipo_documento = request.POST.get("tipo_documento")
        paciente.sexo = request.POST.get("sexo")
        paciente.telefono = request.POST.get("telefono")
        paciente.telefono_adicional = request.POST.get("telefono_adicional")
        paciente.email = request.POST.get("email")
        paciente.calle = request.POST.get("calle")
        paciente.numero = request.POST.get("numero")
        paciente.puerta = request.POST.get("puerta")
        paciente.pais = request.POST.get("pais")
        paciente.ciudad = request.POST.get("ciudad")
        paciente.cp = request.POST.get("cp")
        paciente.aseguradora = request.POST.get("aseguradora")
        paciente.numero_seguro = request.POST.get("numero_seguro")
        paciente.otros_datos = request.POST.get("otros_datos")
        paciente.save()
        if paciente:
            print("Paciente creado")
            return render(request, "app/paciente/paciente_file.html", {"paciente": paciente})
        else:
            print("Error al crear el paciente")
            return render(request, "app/paciente/paciente_new.html")
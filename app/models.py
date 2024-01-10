from django.db import models

# Create your models here.
def paciente_view(request):
    return render(request, 'paciente/paciente.html')
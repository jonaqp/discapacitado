# coding=utf-8
from django.db.models import Q
from rest_framework.generics import ListAPIView

from discapacitado.paciente.models import (
    PacienteAdmision
)
from .serializers import (
    ListaPatientAdmissionSerializer)


class ListaPatientAdmissionAPI(ListAPIView):
    serializer_class = ListaPatientAdmissionSerializer

    def get_queryset(self):
        search_param = self.request.GET.get('q', '')
        if search_param:
            if len(search_param) >= 1:
                queryset = PacienteAdmision.objects.filter(
                    Q(nombres__icontains=search_param) |
                    Q(apellido_paterno__icontains=search_param) |
                    Q(apellido_materno__icontains=search_param)
                )
            else:
                queryset = []
        else:
            queryset = PacienteAdmision.objects.all()
        return queryset

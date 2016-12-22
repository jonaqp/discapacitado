# coding=utf-8
from rest_framework import serializers

from discapacitado.paciente.models import (
    PacienteAdmision
)


class ListaPatientAdmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PacienteAdmision
        exclude = []

from rest_framework import serializers

from discapacitado.establecimiento.models import Establecimiento


class ListaEstablecimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Establecimiento
        exclude = []

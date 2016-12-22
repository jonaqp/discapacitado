# coding=utf-8
from rest_framework import serializers

from discapacitado.catalogo.models import (
    CatalogoCIE, CatalogoDeficiencia,
    CatalogoDiscapacidad, CatalogoProcedimiento
)


class ListaCatalogoCIESerializer(serializers.ModelSerializer):
    class Meta:
        model = CatalogoCIE
        exclude = []


class ListaCatalogoProcedimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatalogoProcedimiento
        exclude = []


class ListaCatalogoDeficienciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatalogoDeficiencia
        exclude = []


class ListaCatalogoDiscapacidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatalogoDiscapacidad
        exclude = []

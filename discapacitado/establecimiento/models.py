# coding=utf-8
from django.core.validators import RegexValidator
from django.db import models

from discapacitado.common import constants as core_constants
from discapacitado.common.models import BaseModel2
from discapacitado.ubigeo.models import (
    UbigeoContinente, UbigeoDepartamento, UbigeoDistrito, UbigeoLocalidad,
    UbigeoPais, UbigeoProvincia)


class Diresa(BaseModel2):
    nombre = models.CharField('Nombre', max_length=100)
    codigo = models.CharField(blank=True, max_length=3, null=True)

    class Meta:
        verbose_name_plural = '1. Diresas'

    def __str__(self):
        return self.nombre


class Red(BaseModel2):
    diresa = models.ForeignKey(Diresa,
                               related_name='%(app_label)s_%(class)s_diresa')
    codigo = models.CharField(max_length=5, validators=[
        RegexValidator(
            regex='^[0-9]{2}$',
            message='Numero de 2 digitos',
        ),
    ], null=True, blank=True)
    nombre = models.CharField('Nombre', max_length=100, null=False)
    estado = models.CharField(
        'Estados', max_length=20, choices=core_constants.STATUS_MODEL,
        null=True, blank=True
    )

    class Meta:
        verbose_name_plural = '2. Redes'

    def __str__(self):
        return self.nombre


class Microred(BaseModel2):
    diresa = models.ForeignKey(Diresa,
                               related_name='%(app_label)s_%(class)s_diresa')
    red = models.ForeignKey(Red, related_name='%(app_label)s_%(class)s_red')
    codigo = models.CharField(max_length=5, validators=[
        RegexValidator(
            regex='^[0-9]{2}$',
            message='Numero de 2 digitos',
        ),
    ], null=True, blank=True)
    nombre = models.CharField('Nombre', max_length=100)
    estado = models.CharField(
        'Estados', max_length=20, choices=core_constants.STATUS_MODEL,
        null=True, blank=True
    )

    class Meta:
        verbose_name_plural = '3. Micro-Redes'

    def __str__(self):
        return self.nombre


class EstablecimientoCategoria(BaseModel2):
    nombre_categoria = models.CharField(verbose_name='nombre categoria',
                                        max_length=15)
    categoria_nivel = models.IntegerField(verbose_name='nivel establecimiento',
                                          blank=True, null=True)

    class Meta:
        verbose_name_plural = '5. Establecimiento Categoria'

    def __str__(self):
        return self.nombre_categoria


class Establecimiento(BaseModel2):
    diresa = models.ForeignKey(
        Diresa, related_name='%(app_label)s_%(class)s_diresa')
    red = models.ForeignKey(Red, related_name='%(app_label)s_%(class)s_red')
    microred = models.ForeignKey(
        Microred, related_name='%(app_label)s_%(class)s_microred')
    codigo_renaes = models.CharField('Código Renaes', max_length=50)
    telefono = models.CharField('Teléfono', max_length=20, blank=True)
    nombre = models.CharField('Nombre', max_length=150)
    descripcion = models.TextField(
        'Descripción', max_length=150, blank=True, null=True)
    codigo_his = models.CharField(
        'Código HIS', max_length=10, null=True, blank=True)
    lote = models.SmallIntegerField('Lote', null=False, default=0)
    location = models.CharField(
        "longitude/latitude", max_length=100, null=True, blank=True)
    categoria = models.ForeignKey(
        EstablecimientoCategoria, blank=True, null=True,
        related_name='%(app_label)s_%(class)s_categoria')
    ubigeo = models.CharField(verbose_name='ubigeo', max_length=8, blank=True,
                              null=True)
    continente = models.ForeignKey(
        UbigeoContinente, related_name='%(app_label)s_%(class)s_continente',
        null=True, blank=True)
    pais = models.ForeignKey(
        UbigeoPais, related_name='%(app_label)s_%(class)s_pais', null=True,
        blank=True)
    departamento = models.ForeignKey(
        UbigeoDepartamento, related_name='%(app_label)s_%(class)s_departamento',
        null=True, blank=True)
    distrito = models.ForeignKey(
        UbigeoDistrito, related_name='%(app_label)s_%(class)s_distrito',
        null=True, blank=True)
    provincia = models.ForeignKey(
        UbigeoProvincia, related_name='%(app_label)s_%(class)s_provincia',
        null=True, blank=True)

    def __str__(self):
        return "{0}-{1}".format(str(self.codigo_renaes), str(self.nombre))

    class Meta:
        verbose_name_plural = '4. Establecimientos'

    @property
    def microred_nombre(self):
        return self.microred.nombre

    @property
    def categoria_nombre(self):
        return self.categoria.nombre_categoria

    @property
    def categoria_nivel(self):
        return self.categoria.categoria_nivel

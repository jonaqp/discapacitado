from django.contrib import admin

from . import forms
from .models import (
    Establecimiento, Diresa, Red, Microred, EstablecimientoCategoria
)


@admin.register(Diresa)
class DiresaAdmin(admin.ModelAdmin):
    ordering = ['nombre']
    search_fields = ['nombre']
    pass


@admin.register(Red)
class RedAdmin(admin.ModelAdmin):
    ordering = ['nombre']
    search_fields = ['nombre']
    pass


@admin.register(Microred)
class MicroredAdmin(admin.ModelAdmin):
    ordering = ['nombre']
    search_fields = ['nombre']


@admin.register(Establecimiento)
class EstablecimientoAdmin(admin.ModelAdmin):
    form = forms.LocationForm
    ordering = ['nombre']
    search_fields = ['nombre']

    fieldsets = (
        (None, {
            'fields': (
                ('diresa', 'red', 'microred'),
                'codigo_renaes', 'categoria', 'nombre', 'location',
            )
        }),
    )


@admin.register(EstablecimientoCategoria)
class EstablecimientoCategoriaAdmin(admin.ModelAdmin):
    ordering = ['nombre_categoria']
    search_field = ['nombre_categoria']

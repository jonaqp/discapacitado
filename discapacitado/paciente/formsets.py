from django.forms import inlineformset_factory

from .forms import (
    PacienteCIEXForm, PacienteDeficienciaForm,
    PacienteDiscapacidadForm, PacienteProcedimientoForm, PacienteCIFForm)
from .models import (
    PacienteConsulta, PacienteCIEX, PacienteDeficiencia, PacienteDiscapacidad,
    PacienteProcedimiento, PacienteCIF
)

PacienteCIEXFormSet = inlineformset_factory(
    PacienteConsulta, PacienteCIEX, form=PacienteCIEXForm,
    extra=0, can_delete=True
)
PacienteDeficienciaFormSet = inlineformset_factory(
    PacienteConsulta, PacienteDeficiencia, form=PacienteDeficienciaForm,
    extra=0, can_delete=True
)
PacienteDiscapacidadFormSet = inlineformset_factory(
    PacienteConsulta, PacienteDiscapacidad, form=PacienteDiscapacidadForm,
    extra=0, can_delete=True
)
PacienteProcedimientoFormSet = inlineformset_factory(
    PacienteConsulta, PacienteProcedimiento, form=PacienteProcedimientoForm,
    extra=0, can_delete=True
)
PacienteCIFFormSet = inlineformset_factory(
    PacienteConsulta, PacienteCIF, form=PacienteCIFForm,
    extra=0, can_delete=True
)

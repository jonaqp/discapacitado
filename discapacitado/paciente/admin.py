from django.contrib import admin

from .models import (
    PacienteAdmision, PacienteAtencion, PacienteCIEX, PacienteCIF,
    PacienteCondicion, PacienteConsulta, PacienteDeficiencia, PacienteDiscapacidad,
    PacienteProcedimiento, PacienteCita
)


@admin.register(PacienteAdmision)
class PatientAdmissionAdmin(admin.ModelAdmin):
    pass


@admin.register(PacienteCita)
class PatientCitaAdmin(admin.ModelAdmin):
    pass


@admin.register(PacienteAtencion)
class PatientAttentionAdmin(admin.ModelAdmin):
    pass


@admin.register(PacienteCIEX)
class PatientCIEXAdmin(admin.ModelAdmin):
    pass


@admin.register(PacienteCIF)
class PatientCIFAdmin(admin.ModelAdmin):
    pass


@admin.register(PacienteCondicion)
class PatientConditionAdmin(admin.ModelAdmin):
    pass


@admin.register(PacienteConsulta)
class PatientConsultAdmin(admin.ModelAdmin):
    pass


@admin.register(PacienteDeficiencia)
class PatientDeficientAdmin(admin.ModelAdmin):
    pass


@admin.register(PacienteDiscapacidad)
class PatientDisabilityAdmin(admin.ModelAdmin):
    pass


@admin.register(PacienteProcedimiento)
class PatientProcedureAdmin(admin.ModelAdmin):
    pass

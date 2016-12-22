from django import forms

from discapacitado.users.models import UserDisponibilidad
from . import constants as paciente_constants
from .models import (
    PacienteAdmision, PacienteConsulta, PacienteCondicion, PacienteAtencion,
    PacienteCIEX,
    PacienteDeficiencia, PacienteDiscapacidad, PacienteCIF,
    PacienteProcedimiento,
    PacienteCita)


class PatientAdmissionForm(forms.ModelForm):
    componente_filiacion = forms.CharField(
        required=False, widget=forms.Select(attrs={"disabled": True}))
    codigo_componente_filiacion = forms.CharField(
        required=False, widget=forms.TextInput(attrs={"disabled": True}))

    def save(self, user=None, *args, **kwargs):
        patient = super().save(*args, **kwargs)
        if user:
            patient.usuario_creacion = user
        patient.save()
        return patient

    class Meta:
        model = PacienteAdmision
        fields = ["tipo_documento", "numero_documento", "nombres",
                  "apellido_paterno", "apellido_materno",
                  "genero", "grado_instruccion", "fecha_nacimiento",
                  "financiador", "numero_hci", "etnia", "componente_filiacion",
                  "codigo_componente_filiacion", "lugar_nacimiento",
                  "distrito_residencial", "distrito_residencial_actual",
                  "direccion_actual", "referencia", "telefono_movil",
                  "correo"]


class PacienteCitaForm(forms.ModelForm):
    seleccion_medico = forms.ChoiceField(
        choices=paciente_constants.SIS_MEDICO_LIST, required=False,
        widget=forms.RadioSelect())
    disponibilidad = forms.ModelChoiceField(
        queryset=UserDisponibilidad.objects.all(),
        widget=forms.HiddenInput())
    tipo_atencion = forms.ChoiceField(
        choices=paciente_constants.TIPO_CITA_CHOICES,
        initial=paciente_constants.CODE_TIPO_CITA_ESPERA,
        widget=forms.HiddenInput()
    )

    class Meta:
        model = PacienteCita
        fields = ["paciente", "area", "disponibilidad", "tipo_atencion"]


class PacienteConsultaForm(forms.ModelForm):
    paciente = forms.ModelChoiceField(
        queryset=PacienteConsulta.objects.all(),
        widget=forms.HiddenInput(), required=False)
    numero_terapia = forms.IntegerField(required=False, initial=0)
    descripcion_terapia = forms.CharField(
        widget=forms.Textarea(), required=False)
    observacion_terapia = forms.CharField(
        widget=forms.Textarea(), required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        initial = kwargs.get('initial', None)
        if initial:
            paciente = PacienteCita.objects.filter(id=initial["paciente"])
            self.fields['paciente'].queryset = paciente

    def save(self, commit=True):
        paciente_consulta = super().save(commit=False)
        if commit:
            paciente_consulta.save()
        return paciente_consulta

    class Meta:
        model = PacienteConsulta
        fields = ["paciente", "fecha", "numero_terapia",
                  "descripcion_terapia", "observacion_terapia"]


class PacienteCondicionForm(forms.ModelForm):
    establecimiento_servicio = forms.CharField(
        required=False, widget=forms.Select())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        initial = kwargs.get('initial', None)
        if initial:
            numero_documento = initial["numero_documento"]
            paciente = PacienteConsulta.objects.filter(
                paciente__numero_documento__exact=numero_documento)
            if paciente.exists():
                self.fields["en_establecimiento"].initial = \
                    paciente_constants.CODE_CONDITION_CONTINUADOR
                self.fields["en_servicio"].initial = \
                    paciente_constants.CODE_CONDITION_CONTINUADOR
            else:
                self.fields["en_establecimiento"].initial = \
                    paciente_constants.CODE_CONDITION_NUEVO
                self.fields["en_servicio"].initial = \
                    paciente_constants.CODE_CONDITION_NUEVO

    def save(self, paciente_consulta=None, *args, **kwargs):
        paciente_condicion = super().save(*args, **kwargs)
        if paciente_consulta:
            paciente_condicion.paciente_consulta = paciente_consulta
        paciente_condicion.save()
        return paciente_condicion

    class Meta:
        model = PacienteCondicion
        fields = ["en_establecimiento", "referencia_establecimiento",
                  "en_servicio", "establecimiento_servicio"]


class PacienteAtencionForm(forms.ModelForm):
    ayuda_tecnica = forms.ChoiceField(
        label="Ayuda Técnica", required=False,
        choices=paciente_constants.AYUDA_TECNICA_CHOICES)
    accidente_dano = forms.ChoiceField(
        label="Accidente/Daño", required=False,
        choices=paciente_constants.ACC_DANIO_CHOICES)
    tiempo_discapacidad_anio = forms.IntegerField(
        label="T.Discapacidad Año", required=False, initial=0)
    tiempo_discapacidad_mes = forms.IntegerField(
        label="T.Discapacidad Mes", required=False, initial=0)
    tiempo_discapacidad_dia = forms.IntegerField(
        label="T.Discapacidad Dia", required=False, initial=0)
    tstdd_anio = forms.IntegerField(
        label="Tstdd Año", required=False, initial=0)
    tstdd_mes = forms.CharField(
        label="Tstdd Mes", required=False, initial=0)
    tstdd_dia = forms.IntegerField(
        label="Tstdd Dia", required=False, initial=0)

    def save(self, paciente_consulta=None, *args, **kwargs):
        paciente_atencion = super().save(*args, **kwargs)
        if paciente_consulta:
            paciente_atencion.paciente_consulta = paciente_consulta
        paciente_atencion.save()
        return paciente_atencion

    class Meta:
        model = PacienteAtencion
        fields = ["ayuda_tecnica", "accidente_dano",
                  "tiempo_discapacidad_anio", "tiempo_discapacidad_mes",
                  "tiempo_discapacidad_dia",
                  "tstdd_anio", "tstdd_mes", "tstdd_dia"]


class PacienteCIEXForm(forms.ModelForm):
    codigo_ciex = forms.CharField(widget=forms.HiddenInput())
    descripcion = forms.CharField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['codigo_ciex'].widget.attrs.update(
            {'readonly': True, 'class': 'form-control'})
        self.fields['descripcion'].widget.attrs.update(
            {'readonly': True, 'class': 'form-control'})

    class Meta:
        model = PacienteCIEX
        fields = ["codigo_ciex"]


class PacienteDeficienciaForm(forms.ModelForm):
    codigo_deficiencia = forms.CharField(widget=forms.HiddenInput())
    descripcion = forms.CharField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['codigo_deficiencia'].widget.attrs.update(
            {'readonly': True, 'class': 'form-control'})
        self.fields['descripcion'].widget.attrs.update(
            {'readonly': True, 'class': 'form-control'})

    class Meta:
        model = PacienteDeficiencia
        fields = ["codigo_deficiencia"]


class PacienteDiscapacidadForm(forms.ModelForm):
    codigo_discapacidad = forms.CharField(widget=forms.HiddenInput())
    descripcion = forms.CharField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['codigo_discapacidad'].widget.attrs.update(
            {'readonly': True, 'class': 'form-control'})
        self.fields['descripcion'].widget.attrs.update(
            {'readonly': True, 'class': 'form-control'})

    class Meta:
        model = PacienteDiscapacidad
        fields = ["codigo_discapacidad"]


class PacienteProcedimientoForm(forms.ModelForm):
    codigo_cpt = forms.CharField(widget=forms.HiddenInput())
    descripcion = forms.CharField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['codigo_cpt'].widget.attrs.update(
            {'readonly': True, 'class': 'form-control'})
        self.fields['descripcion'].widget.attrs.update(
            {'readonly': True, 'class': 'form-control'})

    class Meta:
        model = PacienteProcedimiento
        fields = ["codigo_cpt"]


class PacienteCIFForm(forms.ModelForm):
    codigo_cif = forms.CharField(widget=forms.HiddenInput())
    descripcion = forms.CharField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['codigo_cif'].widget.attrs.update(
            {'readonly': True, 'class': 'form-control'})
        self.fields['descripcion'].widget.attrs.update(
            {'readonly': True, 'class': 'form-control'})

    class Meta:
        model = PacienteCIF
        fields = ["codigo_cif"]

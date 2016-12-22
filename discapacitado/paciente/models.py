import uuid
from datetime import datetime

from dateutil.relativedelta import relativedelta
from django.db import models

from discapacitado.common.models import BaseModel2
from discapacitado.users.models import UserDisponibilidad
from . import constants as paciente_constants


# Create your models here.
class PacienteAdmision(BaseModel2):
    tipo_documento = models.CharField(
        max_length=10, null=False, blank=False,
        choices=paciente_constants.SIS_TYPE_DOC_LIST,
        default=paciente_constants.CODE_TYPE_DOC_DNI
    )
    uid = models.UUIDField(editable=False, default=uuid.uuid4)
    numero_documento = models.CharField(
        max_length=20, unique=True, null=False, blank=False, default='')
    nombres = models.CharField(
        max_length=100, null=True, blank=True, default='')
    apellido_paterno = models.CharField(
        max_length=100, null=True, blank=True, default='')
    apellido_materno = models.CharField(
        max_length=100, null=True, blank=True, default='')
    genero = models.CharField(
        max_length=2, choices=paciente_constants.SEXO_CHOICES,
        default='', null=True, blank=True)
    grado_instruccion = models.CharField(
        max_length=10, null=True, blank=True,
        choices=paciente_constants.GRADO_INSTRUCION_CHOICES)
    fecha_nacimiento = models.DateField(
        null=True, blank=True)
    financiador = models.CharField(
        max_length=10, null=True, blank=True,
        choices=paciente_constants.SIS_FINANCIADOR_LIST,
        default=paciente_constants.CODE_FINANCIADOR_NULO)
    numero_hci = models.CharField(
        max_length=50, null=True, blank=True)
    etnia = models.CharField(
        max_length=5, choices=paciente_constants.ETNIA_CHOICES,
        null=True, blank=True)
    componente_filiacion = models.CharField(
        max_length=50, null=True, blank=True)
    codigo_componente_filiacion = models.CharField(
        max_length=50, null=True, blank=True)
    lugar_nacimiento = models.CharField(
        max_length=100, null=True, blank=True)
    distrito_residencial = models.CharField(
        max_length=100, null=True, blank=True)
    distrito_residencial_actual = models.CharField(
        max_length=100, null=True, blank=True)
    direccion_actual = models.CharField(
        max_length=100, null=True, blank=True)
    referencia = models.CharField(
        max_length=100, null=True, blank=True)
    telefono_movil = models.CharField(
        max_length=10, null=True, blank=True)
    correo = models.EmailField(null=True, blank=True)

    class Meta:
        verbose_name_plural = '1. Paciente Admision'

    @property
    def edad(self):
        str_age = ''
        age = relativedelta(datetime.now().date(), self.fecha_nacimiento)
        if age:
            if age.years < 1:
                str_age = '{month} meses {day} dias'.format(year=age.years,
                                                            month=age.months,
                                                            day=age.days)
            else:
                str_age = '{year} años {month} meses {day} dias'.format(
                    year=age.years, month=age.months, day=age.days)
        return str_age

    @property
    def get_edad(self):
        age = relativedelta(datetime.now().date(), self.fecha_nacimiento)
        return age

    @property
    def get_paciente_edit(self):
        paciente_edit = PacienteAdmision.objects.get(pk=self)
        return paciente_edit

    def __str__(self):
        return "{0} - {1} {2} {3}".format(
            str(self.numero_documento), str(self.nombres).capitalize(),
            str(self.apellido_paterno).capitalize(),
            str(self.apellido_materno).capitalize())


class PacienteCita(BaseModel2):
    paciente = models.ForeignKey(
        PacienteAdmision, related_name='%(app_label)s_%(class)s_paciente')
    area = models.CharField(
        max_length=10, null=False, blank=False,
        choices=paciente_constants.SIS_AREA_LIST,
        default=paciente_constants.CODE_AREA_REHABILITACION)
    disponibilidad = models.ForeignKey(
        UserDisponibilidad,
        related_name='%(app_label)s_%(class)s_disponibilidad')
    tipo_atencion = models.CharField(
        max_length=10, choices=paciente_constants.TIPO_CITA_CHOICES,
        default=paciente_constants.CODE_TIPO_CITA_ESPERA)

    class Meta:
        verbose_name_plural = '2. Paciente Cita'

    def __str__(self):
        return self.paciente.numero_documento


class PacienteConsulta(BaseModel2):
    paciente = models.ForeignKey(
        PacienteCita,
        related_name='%(app_label)s_%(class)s_paciente_cita')
    fecha = models.DateField()
    numero_terapia = models.PositiveSmallIntegerField(default=0)
    descripcion_terapia = models.TextField(null=True, blank=True)
    observacion_terapia = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = '3. Paciente Consulta'

    def __str__(self):
        return "{0}-{1}".format(str(self.paciente), str(self.fecha))


class PacienteCondicion(BaseModel2):
    paciente_consulta = models.ForeignKey(
        PacienteConsulta,
        related_name='%(app_label)s_%(class)s_paciente_consulta')
    en_establecimiento = models.CharField(
        max_length=10, null=True, blank=True,
        choices=paciente_constants.SIS_CONDITION_LIST,
        default=paciente_constants.CODE_CONDITION_NUEVO)
    referencia_establecimiento = models.CharField(
        max_length=10, null=True, blank=True,
        choices=paciente_constants.TIPO_REFERENCIA,
        default=paciente_constants.CODE_REFERENCIA_NULO)
    en_servicio = models.CharField(
        max_length=10, null=True, blank=True,
        choices=paciente_constants.SIS_CONDITION_LIST,
        default=paciente_constants.CODE_CONDITION_NUEVO)
    establecimiento_servicio = models.CharField(
        max_length=10, null=True, blank=True)

    class Meta:
        verbose_name_plural = '4. Paciente Condicion'

    def __str__(self):
        return str(self.paciente_consulta)


class PacienteAtencion(BaseModel2):
    paciente_consulta = models.ForeignKey(
        PacienteConsulta,
        related_name='%(app_label)s_%(class)s_paciente_consulta')
    ayuda_tecnica = models.CharField(max_length=10, null=True, blank=True)
    accidente_dano = models.CharField(max_length=10, null=True, blank=True)
    tiempo_discapacidad_anio = models.PositiveSmallIntegerField(
        null=True, blank=True, default=0)
    tiempo_discapacidad_mes = models.PositiveSmallIntegerField(
        null=True, blank=True, default=0)
    tiempo_discapacidad_dia = models.PositiveSmallIntegerField(
        null=True, blank=True, default=0)
    tstdd_anio = models.PositiveSmallIntegerField(
        null=True, blank=True, default=0)
    tstdd_mes = models.PositiveSmallIntegerField(
        null=True, blank=True, default=0)
    tstdd_dia = models.PositiveSmallIntegerField(
        null=True, blank=True, default=0)
    is_discapacidad_nacido = models.BooleanField(
        default=False)

    class Meta:
        verbose_name_plural = '5. Paciente Atencion'

    def __str__(self):
        return str(self.paciente_consulta)


class PacienteCIEX(BaseModel2):
    paciente_consulta = models.ForeignKey(
        PacienteConsulta,
        related_name='%(app_label)s_%(class)s_paciente_consulta')
    codigo_ciex = models.CharField(max_length=10, null=False, blank=False)
    descripcion = models.CharField(max_length=200, null=False, blank=False)

    class Meta:
        verbose_name_plural = '6. Paciente CIEX'

    def __str__(self):
        return str(self.paciente_consulta)


class PacienteDeficiencia(BaseModel2):
    paciente_consulta = models.ForeignKey(
        PacienteConsulta,
        related_name='%(app_label)s_%(class)s_paciente_consulta')
    codigo_deficiencia = models.CharField(
        max_length=10, null=False, blank=False)
    descripcion = models.CharField(max_length=200, null=False, blank=False)
    gravedad = models.CharField(max_length=10, null=False, blank=False)

    class Meta:
        verbose_name_plural = '7. Paciente Deficiencia'

    def __str__(self):
        return str(self.paciente_consulta)


class PacienteDiscapacidad(BaseModel2):
    paciente_consulta = models.ForeignKey(
        PacienteConsulta,
        related_name='%(app_label)s_%(class)s_paciente_consulta')
    codigo_discapacidad = models.CharField(
        max_length=10, null=False, blank=False)
    descripcion = models.CharField(
        max_length=200, null=False, blank=False)

    class Meta:
        verbose_name_plural = '8. Paciente Capacidad'

    def __str__(self):
        return str(self.paciente_consulta)


class PacienteCIF(BaseModel2):
    paciente_consulta = models.ForeignKey(
        PacienteConsulta,
        related_name='%(app_label)s_%(class)s_paciente_consulta')
    codigo_cif = models.CharField(max_length=10, null=False, blank=False)
    descripcion = models.CharField(max_length=200, null=False, blank=False)

    class Meta:
        verbose_name_plural = '9. Paciente CIF'

    def __str__(self):
        return str(self.paciente_consulta)


class PacienteProcedimiento(BaseModel2):
    paciente_consulta = models.ForeignKey(
        PacienteConsulta,
        related_name='%(app_label)s_%(class)s_paciente_consulta')
    codigo_cpt = models.CharField(
        max_length=10, null=False, blank=False)
    descripcion = models.CharField(max_length=200, null=False, blank=False)

    class Meta:
        verbose_name_plural = '10. Paciente Procedimiento'

    def __str__(self):
        return str(self.paciente_consulta)

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

from discapacitado.common.models import BaseModel2, Turno
from discapacitado.establecimiento.models import Establecimiento


class User(AbstractUser):
    name = models.CharField(_('Name of User'), blank=True, max_length=255)

    def get_groups(self):
        return ", ".join([p.name for p in self.groups.all()])

    class Meta:
        db_table = 'auth_user'
        verbose_name_plural = '1. Usuarios'

    def __str__(self):
        return self.username


class UserEstablecimiento(BaseModel2):
    usuario = models.ForeignKey(
        User, related_name='%(app_label)s_%(class)s_usuario')
    establecimiento = models.ManyToManyField(
        Establecimiento, related_name='%(app_label)s_%(class)s_establecimiento')

    def get_usuario_establecimiento_lista(self):
        return ", ".join([p.codigo_renaes for p in self.establecimiento.all()])

    def __str__(self):
        return "{0}".format(str(self.usuario))

    class Meta:
        unique_together = ["usuario"]
        verbose_name_plural = '2. Usuarios Establecimientos'


class UserCupo(BaseModel2):
    usuario = models.ForeignKey(
        User, related_name='%(app_label)s_%(class)s_usuario')
    fecha = models.DateField(
        help_text="fecha empezando el mes, ejemplo:2016-11-01")
    cupo = models.PositiveSmallIntegerField(default=10)
    establecimiento = models.ForeignKey(
        Establecimiento, related_name='%(app_label)s_%(class)s_establecimiento')

    def __str__(self):
        return "{0}".format(str(self.usuario))

    class Meta:
        unique_together = ["usuario", "fecha", "cupo", "establecimiento"]
        verbose_name_plural = '3. Usuarios Cupos'


class UserDisponibilidad(BaseModel2):
    usuario = models.ForeignKey(
        User, related_name='%(app_label)s_%(class)s_usuario')
    turno = models.ForeignKey(
        Turno, related_name='%(app_label)s_%(class)s_turno')
    horario = models.DateTimeField(blank=False)
    establecimiento = models.ForeignKey(
        Establecimiento, related_name='%(app_label)s_%(class)s_establecimiento')

    def get_month_horario(self):
        return self.horario.strftime("%m")

    class Meta:
        unique_together = ["usuario", "turno", "horario", "establecimiento"]
        verbose_name_plural = '4. Usuario Disponibilidades'

    def __str__(self):
        return "{0}-{1}-{2}".format(str(self.usuario),
                                    str(self.turno),
                                    str(self.horario))

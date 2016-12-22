import datetime
import uuid

from django.conf import settings
from django.db import models

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class TimeStampedModel(models.Model):
    fecha_creacion = models.DateTimeField(
        blank=True, null=True, editable=False, auto_now_add=True)
    fecha_modificacion = models.DateTimeField(
        blank=True, null=True, editable=False, auto_now=True)
    usuario_creacion = models.ForeignKey(
        AUTH_USER_MODEL, editable=False, null=True,
        related_name="%(app_label)s_%(class)s_usuario_creacion")

    def save(self, *args, **kwargs):
        if self.id:
            self.fecha_modificacion = datetime.datetime.now()
        else:
            self.fecha_creacion = datetime.datetime.now()
            kwargs['force_insert'] = False
        super().save(*args, **kwargs)

    class Meta:
        abstract = True


class Turno(models.Model):
    nombre = models.CharField(max_length=200, null=False, blank=False)
    abreviatura = models.CharField(max_length=10, null=False, blank=False)

    class Meta:
        unique_together = ["nombre", "abreviatura"]
        verbose_name_plural = '1. Turnos'

    def __str__(self):
        return self.nombre


class UUIDModel(models.Model):
    """ Modelo abstracto field uuid """
    uid = models.UUIDField(editable=False, default=uuid.uuid4)

    class Meta:
        abstract = True


class StatusModel(models.Model):
    """ Modelo abstracto boleano para el registro """
    es_removido = models.BooleanField(default=False, editable=False)

    class Meta:
        abstract = True


class BaseModel(UUIDModel, TimeStampedModel, StatusModel):
    """ Modelo Inherente para abstraer campos con uuid """

    class Meta:
        abstract = True


class BaseModel2(TimeStampedModel, StatusModel):
    """ Modelo Inherente para abstraer campos sin uuid """

    class Meta:
        abstract = True

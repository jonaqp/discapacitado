# coding=utf-8
from django.conf.urls import url

from .views import (
    ListaPatientAdmissionAPI
)

urlpatterns = [
    url(r'^paciente/admision/lista/$',
        ListaPatientAdmissionAPI.as_view()),

]

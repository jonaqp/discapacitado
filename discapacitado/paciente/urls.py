from django.conf.urls import url, include

from . import views


urlpatterns = [
    url(r'^establecimiento/$',
        views.EstablishmentView.as_view(),
        name='establecimiento'),

    url(r'^$',
        views.DashboardView.as_view(),
        name='dashboard'),

    url(r'^admision/',
        include([
            url(r'^$',
                views.AdmisionList.as_view(), name='list'),
            url(r'^nuevo/$',
                views.AdmisionCreation.as_view(), name='create'),
            url(r'^(?P<pk>\d+)/actualizar/$',
                views.AdmisionUpdate.as_view(), name='update'),
        ], namespace='admision')),

    url(r'^cita/',
        include([
            url(r'^$',
                views.CitaList.as_view(), name='list'),
            url(r'^nuevo/$',
                views.CitaCreation.as_view(), name='create'),
            url(r'^(?P<pk>\d+)/actualizar/$',
                views.CitaUpdate.as_view(), name='update'),
            url(r'^lista-medico/$',
                views.CitaListaMedicoAjaxView.as_view(),
                name='lista-medico'),
            url(r'^lista-medico-disponibilidad/$',
                views.CitaListaMedicoDisponibilidadAjaxView.as_view(),
                name='lista-medico-disponibilidad'),

        ], namespace='cita')),

    url(r'^medico/',
        include([
            url(r'^$',
                views.MedicoList.as_view(), name='list'),
            url(r'^(?P<pk>\d+)/nuevo/$',
                views.MedicoCreation.as_view(), name='create'),
            url(r'^(?P<pk>\d+)/actualizar/$',
                views.MedicoUpdate.as_view(), name='update'),
        ], namespace='medico')),

    url(r'^tecnologo/',
        include([
            url(r'^$',
                views.TecnologoList.as_view(), name='list'),
            url(r'^(?P<pk>\d+)/nuevo/$',
                views.TecnologoCreation.as_view(), name='create'),
            url(r'^(?P<pk>\d+)/actualizar/$',
                views.TecnologoUpdate.as_view(), name='update'),
        ], namespace='tecnologo')),



]

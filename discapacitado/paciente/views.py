# Create your views here.

import datetime

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic import UpdateView

from discapacitado.establecimiento.models import Establecimiento
from discapacitado.users.forms import UserEstablishmentForm
from discapacitado.users.models import (
    User, UserEstablecimiento, UserDisponibilidad, UserCupo)
from . import constants as paciente_constants
from .forms import (
    PatientAdmissionForm, PacienteCitaForm, PacienteConsultaForm,
    PacienteCondicionForm, PacienteAtencionForm)
from .formsets import PacienteCIEXFormSet, PacienteDeficienciaFormSet, \
    PacienteDiscapacidadFormSet, PacienteCIFFormSet, \
    PacienteProcedimientoFormSet
from .models import PacienteAdmision, PacienteCita, PacienteConsulta


class EstablishmentView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/establecimiento.html'

    def get(self, request, *args, **kwargs):
        _establecimiento = request.session.get('actual_establecimiento', None)
        if _establecimiento:
            return redirect('paciente-app:admision:list')
        user_session = self.request.user
        user = User.objects.get(username=user_session)
        self.establishment_form = UserEstablishmentForm(initial={"user": user})
        return super().render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        establecimiento = request.POST.get("establecimiento")
        if establecimiento:
            self.request.session['actual_establecimiento'] = establecimiento
            return redirect('paciente-app:admision:list')
        else:
            return redirect('paciente-app:establecimiento')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["establishment_form"] = self.establishment_form
        return context


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/index.html'


"""
    Admision
"""


class AdmisionList(LoginRequiredMixin, ListView):
    template_name = 'patient/admision/admision_list.html'
    model = PacienteAdmision
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        busqueda = self.request.POST.get("query_search", None)
        if busqueda:
            queryset = PacienteAdmision.objects.filter(
                Q(numero_documento__icontains=busqueda) |
                Q(nombres__icontains=busqueda) |
                Q(apellido_materno__icontains=busqueda) |
                Q(apellido_paterno__icontains=busqueda)
            )
        return queryset

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        _establecimiento = request.session.get('actual_establecimiento', None)
        if not _establecimiento:
            return redirect('paciente-app:establecimiento')
        return super().render_to_response(
            self.get_context_data(object_list=self.object_list))

    def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        return super().render_to_response(
            self.get_context_data(object_list=self.object_list))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(**kwargs)
        context["text_central"] = "Lista Pacientes"
        return context


class AdmisionCreation(LoginRequiredMixin, CreateView):
    template_name = 'patient/admision/admision_form.html'
    model = PacienteAdmision
    success_url = reverse_lazy('paciente-app:cita:list')
    form_class = PatientAdmissionForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["text_central"] = "Crear Paciente"
        return context


class AdmisionUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'patient/admision/admision_form.html'
    model = PacienteAdmision
    success_url = reverse_lazy('paciente-app:admision:list')
    form_class = PatientAdmissionForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["text_central"] = "Actualizar Paciente"
        return context


"""
    Cita
"""


class CitaList(LoginRequiredMixin, ListView):
    template_name = 'patient/cita/cita_list.html'
    model = PacienteCita
    paginate_by = 10

    def get_queryset(self):
        date_now = datetime.datetime.today().date()
        queryset = PacienteCita.objects.filter(
            disponibilidad__horario__gte=date_now)
        busqueda = self.request.POST.get("query_search", None)
        if busqueda:
            queryset = PacienteCita.objects.filter(
                Q(paciente__numero_documento__icontains=busqueda) |
                Q(paciente__nombres__icontains=busqueda) |
                Q(paciente__apellido_materno__icontains=busqueda) |
                Q(paciente__apellido_paterno__icontains=busqueda),
                disponibilidad__horario__gte=date_now
            )
        return queryset

    def get(self, request, *args, **kwargs):
        _establecimiento = request.session.get('actual_establecimiento', None)
        if _establecimiento:
            return redirect('paciente-app:admision:list')
        self.object_list = self.get_queryset()
        return super().render_to_response(
            self.get_context_data(object_list=self.object_list))

    def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        return super().render_to_response(
            self.get_context_data(object_list=self.object_list))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(**kwargs)
        context["text_central"] = "Lista Pacientes Cita"
        return context


class CitaCreation(LoginRequiredMixin, CreateView):
    template_name = 'patient/cita/cita_form.html'
    model = PacienteCita
    success_url = reverse_lazy('paciente-app:cita:list')
    form_class = PacienteCitaForm

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        self.form = self.get_form(form_class)
        return super().render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        disponibilidad = request.POST.get("disponibilidad", None)
        _establecimiento = request.session.get('actual_establecimiento', None)

        establecimiento = Establecimiento.objects.get(
            codigo_renaes=_establecimiento)
        self.usuario_disponibilidad = UserDisponibilidad.objects.get(
            id=disponibilidad)
        actual_mes = self.usuario_disponibilidad.get_month_horario()
        user_cupo = UserCupo.objects.get(
            usuario=self.usuario_disponibilidad.usuario,
            fecha__month=actual_mes,
            establecimiento=establecimiento)
        paciente_cita = PacienteCita.objects.filter(
            disponibilidad__usuario=self.usuario_disponibilidad.usuario,
            disponibilidad__horario__month=actual_mes,
            disponibilidad__establecimiento=establecimiento).count()
        if int(paciente_cita) >= int(user_cupo.cupo):
            messages.add_message(
                request, messages.INFO,
                'Ya no tiene cupo el medico: {0:s}'.format(
                    self.usuario_disponibilidad.usuario.first_name))
            return redirect('paciente-app:cita:create')
        if form.is_valid():
            return self.frm_valid(form)
        else:
            return self.frm_invalid(form)

    def frm_valid(self, form):
        with transaction.atomic():
            self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())

    def frm_invalid(self, form):
        self.form = form
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form
        context["text_central"] = "Crear Paciente Cita"
        return context


class CitaUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'patient/cita/cita_form.html'
    model = PacienteCita
    success_url = reverse_lazy('paciente-app:cita:list')
    form_class = PacienteCitaForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["text_central"] = "Actualizar Paciente Cita"
        return context


class CitaListaMedicoAjaxView(TemplateView):
    template_name = 'patient/cita/ajax/citas_lista_medico.html'

    def get(self, request, *args, **kwargs):
        tipo_medico = request.GET.get("tipo_medico")
        new_dict = dict(paciente_constants.SIS_MEDICO_LIST)
        self.new_result_medico = str(new_dict[tipo_medico]).lower()
        _establecimiento = request.session.get('actual_establecimiento')
        self.lista_medico = UserEstablecimiento.objects.filter(
            usuario__groups__name=self.new_result_medico,
            establecimiento=_establecimiento)
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["lista_medico"] = self.lista_medico
        context["tipo_medico"] = self.new_result_medico
        return context


class CitaListaMedicoDisponibilidadAjaxView(TemplateView):
    template_name = 'patient/cita/ajax/citas_lista_medico_disponibilidad.html'

    def get(self, request, *args, **kwargs):
        date_now = datetime.datetime.today().date()
        usuario_id = request.GET.get("usuario_id")
        self.usuario = User.objects.get(id=usuario_id)
        self.lista_disponibilidad = UserDisponibilidad.objects.filter(
            usuario=self.usuario, horario__gte=date_now)
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["lista_disponibilidad"] = self.lista_disponibilidad
        context["usuario"] = self.usuario
        return context


"""
    Medico
"""


class MedicoList(LoginRequiredMixin, ListView):
    template_name = 'patient/medico/medico_list.html'
    model = PacienteConsulta
    paginate_by = 10

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.code_cita_initial = paciente_constants.CODE_TIPO_CITA_ESPERA

    def get_queryset(self):
        date_now = datetime.datetime.today().date()
        user_session = self.request.user
        user = User.objects.get(username=user_session)
        queryset = PacienteCita.objects.filter(
            disponibilidad__horario__gte=date_now,
            disponibilidad__usuario=user)
        busqueda = self.request.POST.get("query_search", None)
        if busqueda:
            queryset = PacienteCita.objects.filter(
                Q(paciente__numero_documento__icontains=busqueda) |
                Q(paciente__nombres__icontains=busqueda) |
                Q(paciente__apellido_materno__icontains=busqueda) |
                Q(paciente__apellido_paterno__icontains=busqueda),
                disponibilidad__horario__gte=date_now,
                disponibilidad__usuario=user
            )
        return queryset

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        return super().render_to_response(
            self.get_context_data(object_list=self.object_list))

    def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        return super().render_to_response(
            self.get_context_data(object_list=self.object_list))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(**kwargs)
        context["text_central"] = "Lista Consultas Medicas"
        context["code_cita_initial"] = self.code_cita_initial
        return context


class MedicoCreation(LoginRequiredMixin, CreateView):
    template_name = 'patient/medico/medico_form.html'
    model = PacienteConsulta
    success_url = reverse_lazy('paciente-app:medico:list')
    form_class = PacienteConsultaForm

    def get_initial(self):
        super().get_initial()
        paciente_id = self.kwargs.get("pk", None)
        self.parameter = dict(paciente=paciente_id)
        return self.parameter

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        self.form = self.get_form(form_class)
        self.paciente = PacienteCita.objects.get(pk=self.kwargs.get("pk"))
        self.form_condicion = PacienteCondicionForm()
        self.form_atencion = PacienteAtencionForm()
        self.formset_ciex = PacienteCIEXFormSet()
        self.formset_deficiencia = PacienteDeficienciaFormSet()
        self.formset_discapacidad = PacienteDiscapacidadFormSet()
        self.formset_cpt = PacienteProcedimientoFormSet()
        self.formset_cif = PacienteCIFFormSet()
        return super().render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        self.paciente = PacienteCita.objects.get(pk=self.kwargs.get("pk"))
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        form_condicion = PacienteCondicionForm(request.POST)
        form_atencion = PacienteAtencionForm(request.POST)
        formset_ciex = PacienteCIEXFormSet(request.POST)
        formset_deficiencia = PacienteDeficienciaFormSet(request.POST)
        formset_discapacidad = PacienteDiscapacidadFormSet(request.POST)
        formset_cif = PacienteCIFFormSet(request.POST)
        formset_cpt = PacienteProcedimientoFormSet(request.POST)

        if form.is_valid() and form_condicion.is_valid() and \
                form_atencion.is_valid() and formset_ciex.is_valid() and \
                formset_deficiencia.is_valid() and \
                formset_discapacidad.is_valid() and formset_cif.is_valid() and \
                formset_cpt.is_valid():
            return self.frm_valid(
                form, form_condicion, form_atencion, formset_ciex,
                formset_deficiencia, formset_discapacidad, formset_cif,
                formset_cpt
            )
        else:
            return self.frm_invalid(
                form, form_condicion, form_atencion, formset_ciex,
                formset_deficiencia, formset_discapacidad, formset_cif,
                formset_cpt
            )

    def frm_valid(
            self, form, form_condicion, form_atencion, formset_ciex,
            formset_deficiencia, formset_discapacidad, formset_cif,
            formset_cpt):
        with transaction.atomic():
            self.object = form.save()
            form_condicion.save(paciente_consulta=self.object, commit=False)
            form_atencion.save(paciente_consulta=self.object, commit=False)
            formset_ciex.instance = self.object
            formset_ciex.save()
            formset_deficiencia.instance = self.object
            formset_deficiencia.save()
            formset_discapacidad.instance = self.object
            formset_discapacidad.save()
            formset_cif.instance = self.object
            formset_cif.save()
            formset_cpt.instance = self.object
            formset_cpt.save()
            self.paciente.tipo_atencion = paciente_constants.CODE_TIPO_CITA_ATENDIDO
            self.paciente.save()
        return HttpResponseRedirect(self.get_success_url())

    def frm_invalid(
            self, form, form_condicion, form_atencion, formset_ciex,
            formset_deficiencia, formset_discapacidad, formset_cif,
            formset_cpt):
        self.form = form
        self.form_condicion = form_condicion
        self.form_atencion = form_atencion
        self.formset_ciex = formset_ciex
        self.formset_deficiencia = formset_deficiencia
        self.formset_discapacidad = formset_discapacidad
        self.formset_cif = formset_cif
        self.formset_cpt = formset_cpt
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form
        context["paciente"] = self.paciente
        context["form_condicion"] = self.form_condicion
        context["form_atencion"] = self.form_atencion
        context["formset_ciex"] = self.formset_ciex
        context["formset_deficiencia"] = self.formset_deficiencia
        context["formset_discapacidad"] = self.formset_discapacidad
        context["formset_cif"] = self.formset_cif
        context["formset_cpt"] = self.formset_cpt
        context["text_central"] = "Crear Consulta Medica"
        return context


class MedicoUpdate(LoginRequiredMixin, TemplateView):
    template_name = 'patient/medico/medico_form.html'

    def get(self, request, *args, **kwargs):
        instance = PacienteCita.objects.get(pk=self.kwargs.get('pk'))
        instance.tipo_atencion = paciente_constants.CODE_TIPO_CITA_CANCELADO
        instance.save()
        return HttpResponseRedirect(reverse_lazy('paciente-app:medico:list'))


"""
    Tecnologo
"""


class TecnologoList(LoginRequiredMixin, ListView):
    template_name = 'patient/tecnologo/tecnologo_list.html'
    model = PacienteConsulta
    paginate_by = 10

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.code_cita_initial = paciente_constants.CODE_TIPO_CITA_ESPERA

    def get_queryset(self):
        date_now = datetime.datetime.today().date()
        user_session = self.request.user
        user = User.objects.get(username=user_session)
        queryset = PacienteCita.objects.filter(
            disponibilidad__horario__gte=date_now,
            disponibilidad__usuario=user)
        busqueda = self.request.POST.get("query_search", None)
        if busqueda:
            queryset = PacienteCita.objects.filter(
                Q(paciente__numero_documento__icontains=busqueda) |
                Q(paciente__nombres__icontains=busqueda) |
                Q(paciente__apellido_materno__icontains=busqueda) |
                Q(paciente__apellido_paterno__icontains=busqueda),
                disponibilidad__horario__gte=date_now,
                disponibilidad__usuario=user
            )
        return queryset

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        return super().render_to_response(
            self.get_context_data(object_list=self.object_list))

    def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        return super().render_to_response(
            self.get_context_data(object_list=self.object_list))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(**kwargs)
        context["text_central"] = "Lista Consultas Tecnologo"
        context["code_cita_initial"] = self.code_cita_initial
        return context


class TecnologoCreation(LoginRequiredMixin, CreateView):
    template_name = 'patient/tecnologo/tecnologo_form.html'
    model = PacienteConsulta
    success_url = reverse_lazy('paciente-app:tecnologo:list')
    form_class = PacienteConsultaForm

    def get_initial(self):
        super().get_initial()
        paciente_id = self.kwargs.get("pk", None)
        self.parameter = dict(paciente=paciente_id)
        return self.parameter

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        self.form = self.get_form(form_class)
        self.paciente = PacienteCita.objects.get(pk=self.kwargs.get("pk"))
        self.form_condicion = PacienteCondicionForm()
        self.formset_ciex = PacienteCIEXFormSet()
        self.formset_deficiencia = PacienteDeficienciaFormSet()
        self.formset_discapacidad = PacienteDiscapacidadFormSet()
        self.formset_cpt = PacienteProcedimientoFormSet()
        self.formset_cif = PacienteCIFFormSet()
        return super().render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        self.paciente = PacienteCita.objects.get(pk=self.kwargs.get("pk"))
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        form_condicion = PacienteCondicionForm(request.POST)
        formset_ciex = PacienteCIEXFormSet(request.POST)
        formset_deficiencia = PacienteDeficienciaFormSet(request.POST)
        formset_discapacidad = PacienteDiscapacidadFormSet(request.POST)
        formset_cif = PacienteCIFFormSet(request.POST)
        formset_cpt = PacienteProcedimientoFormSet(request.POST)

        if form.is_valid() and form_condicion.is_valid() and \
                formset_ciex.is_valid() and formset_deficiencia.is_valid() and \
                formset_discapacidad.is_valid() and formset_cif.is_valid() and \
                formset_cpt.is_valid():
            return self.frm_valid(
                form, form_condicion, formset_ciex, formset_deficiencia,
                formset_discapacidad, formset_cif, formset_cpt
            )
        else:
            return self.frm_invalid(
                form, form_condicion, formset_ciex, formset_deficiencia,
                formset_discapacidad, formset_cif, formset_cpt
            )

    def frm_valid(
            self, form, form_condicion, formset_ciex, formset_deficiencia,
            formset_discapacidad, formset_cif, formset_cpt):
        with transaction.atomic():
            self.object = form.save()
            form_condicion.save(paciente_consulta=self.object, commit=False)
            formset_ciex.instance = self.object
            formset_ciex.save()
            formset_deficiencia.instance = self.object
            formset_deficiencia.save()
            formset_discapacidad.instance = self.object
            formset_discapacidad.save()
            formset_cif.instance = self.object
            formset_cif.save()
            formset_cpt.instance = self.object
            formset_cpt.save()
            self.paciente.tipo_atencion = paciente_constants.CODE_TIPO_CITA_ATENDIDO
            self.paciente.save()
        return HttpResponseRedirect(self.get_success_url())

    def frm_invalid(
            self, form, form_condicion, formset_ciex, formset_deficiencia,
            formset_discapacidad, formset_cif, formset_cpt):
        self.form = form
        self.form_condicion = form_condicion
        self.formset_ciex = formset_ciex
        self.formset_deficiencia = formset_deficiencia
        self.formset_discapacidad = formset_discapacidad
        self.formset_cif = formset_cif
        self.formset_cpt = formset_cpt
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form
        context["paciente"] = self.paciente
        context["form_condicion"] = self.form_condicion
        context["formset_ciex"] = self.formset_ciex
        context["formset_deficiencia"] = self.formset_deficiencia
        context["formset_discapacidad"] = self.formset_discapacidad
        context["formset_cif"] = self.formset_cif
        context["formset_cpt"] = self.formset_cpt
        context["text_central"] = "Crear Consulta Tecnologa"
        return context


class TecnologoUpdate(LoginRequiredMixin, TemplateView):
    template_name = 'patient/tecnologo/tecnologo_form.html'

    def get(self, request, *args, **kwargs):
        instance = PacienteCita.objects.get(pk=self.kwargs.get('pk'))
        instance.tipo_atencion = paciente_constants.CODE_TIPO_CITA_CANCELADO
        instance.save()
        return HttpResponseRedirect(reverse_lazy('paciente-app:medico:list'))
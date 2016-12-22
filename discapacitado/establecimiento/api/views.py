# coding=utf-8
import requests
from discapacitado.common.drf_custom import LargeResultsSetPagination
from discapacitado.common.mixins import JSONResponseMixin
from django.conf import settings
from django.db.models import Q
from django.views import View
from rest_framework.generics import ListAPIView

from discapacitado.establecimiento.models import Establecimiento
from .serializers import (
    ListaEstablecimientoSerializer
)

BASE_URL_API = settings.BASE_URL_API


class ListaEstablecimientoJSONAPI(View, JSONResponseMixin):
    def get(self, request):
        search_param = self.request.GET.get('q', '')
        print(search_param)
        data = requests.get(
            '{}?q={}&page_size=10'.format(
                "http://localhost:8006/api/v1/establecimiento/lista/",
                search_param)).json().get('data')
        json_data = []
        for obj_data in data:
            json_data.append(
                {
                    'id': obj_data.get('attributes').get('codigo_renaes'),
                    'text': '{0} - {1}'.format(
                        obj_data.get('attributes').get('codigo_renaes'),
                        obj_data.get('attributes').get('nombre')
                    )
                }
            )
        return self.render_to_json_response(json_data)


class ListaEstablecmientoAPI(ListAPIView):
    serializer_class = ListaEstablecimientoSerializer
    pagination_class = LargeResultsSetPagination

    def get_queryset(self):
        search_param = self.request.GET.get('q', '')
        print(search_param)
        if search_param:
            if len(search_param) >= 3:
                queryset = Establecimiento.objects.filter(
                    Q(codigo_renaes__icontains=search_param) |
                    Q(nombre__icontains=search_param))
            else:
                queryset = []
        else:
            queryset = Establecimiento.objects.all()
        return queryset

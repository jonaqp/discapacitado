# coding=utf-8
import requests
from discapacitado.common.drf_custom import LargeResultsSetPagination
from discapacitado.common.mixins import JSONResponseMixin
from django.db.models import Q
from django.views import View
from rest_framework.generics import ListAPIView

from discapacitado.catalogo.models import (
    CatalogoCIE, CatalogoDeficiencia, CatalogoProcedimiento
)
from .serializers import (
    ListaCatalogoDeficienciaSerializer,
    ListaCatalogoCIESerializer, ListaCatalogoProcedimientoSerializer)


class ListaCatalogoCIEJSONAPI(View, JSONResponseMixin):
    def get(self, request):
        search_param = self.request.GET.get('q', '')
        data = requests.get(
            '{}?q={}&page_size=10'.format(
                "http://localhost:8006/api/v1/catalogo/cie/lista/",
                search_param)).json().get('data')
        json_data = []
        for obj_data in data:
            json_data.append(
                {
                    'id': obj_data.get('attributes').get('id_ciex'),
                    'text': '{0} - {1}'.format(
                        obj_data.get('attributes').get('id_ciex'),
                        obj_data.get('attributes').get('desc_ciex')
                    )
                }
            )
        return self.render_to_json_response(json_data)


class ListaCatalogoCIEAPI(ListAPIView):
    serializer_class = ListaCatalogoCIESerializer
    pagination_class = LargeResultsSetPagination

    def get_queryset(self):
        search_param = self.request.GET.get('q', '')
        if search_param:
            if len(search_param) >= 3:
                queryset = CatalogoCIE.objects.filter(
                    Q(id_ciex__icontains=search_param) | Q(
                        desc_ciex__icontains=search_param))
            else:
                queryset = []
        else:
            queryset = CatalogoCIE.objects.all()
        return queryset


class ListaCatalogoDEFICIENCIAJSONAPI(View, JSONResponseMixin):
    def get(self, request):
        search_param = self.request.GET.get('q', '')
        data = requests.get(
            '{}?q={}&page_size=10'.format(
                "http://localhost:8006/api/v1/catalogo/deficiencia/lista/",
                search_param)).json().get('data')
        json_data = []
        for obj_data in data:
            json_data.append(
                {
                    'id': obj_data.get('attributes').get(
                        'categoria_deficiencia'),
                    'text': '{0} - {1}'.format(
                        obj_data.get('attributes').get('categoria_deficiencia'),
                        obj_data.get('attributes').get('nombre_deficiencia')
                    )
                }
            )
        return self.render_to_json_response(json_data)


class ListaCatalogoDEFICIENCIAAPI(ListAPIView):
    serializer_class = ListaCatalogoDeficienciaSerializer
    pagination_class = LargeResultsSetPagination

    def get_queryset(self):
        search_param = self.request.GET.get('q', '')
        if search_param:
            if len(search_param) >= 1:
                queryset = CatalogoDeficiencia.objects.filter(
                    Q(categoria_deficiencia__icontains=search_param) |
                    Q(nombre_deficiencia__icontains=search_param))
            else:
                queryset = []
        else:
            queryset = CatalogoDeficiencia.objects.all()
        return queryset


class ListaCatalogoPROCEDIMIENTOJSONAPI(View, JSONResponseMixin):
    def get(self, request):
        search_param = self.request.GET.get('q', '')
        data = requests.get(
            '{}?q={}&page_size=10'.format(
                "http://localhost:8006/api/v1/catalogo/procedimiento/lista/",
                search_param)).json().get('data')
        json_data = []
        for obj_data in data:
            json_data.append(
                {
                    'id': obj_data.get('attributes').get('codigo_cpt'),
                    'text': '{0} - {1}'.format(
                        obj_data.get('attributes').get(
                            'codigo_cpt'),
                        obj_data.get('attributes').get(
                            'denominacion_procedimientos')
                    )
                }
            )
        return self.render_to_json_response(json_data)


class ListaCatalogoPROCEDIMIENTOAPI(ListAPIView):
    serializer_class = ListaCatalogoProcedimientoSerializer
    pagination_class = LargeResultsSetPagination

    def get_queryset(self):
        search_param = self.request.GET.get('q', '')
        if search_param:
            if len(search_param) >= 1:
                queryset = CatalogoProcedimiento.objects.filter(
                    Q(codigo_cpt__icontains=search_param) |
                    Q(denominacion_procedimientos__icontains=search_param))
            else:
                queryset = []
        else:
            queryset = CatalogoProcedimiento.objects.all()
        return queryset

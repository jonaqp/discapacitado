# coding=utf-8
from django.conf.urls import url

from .views import (
    ListaCatalogoCIEAPI,
    ListaCatalogoCIEJSONAPI,
    ListaCatalogoDEFICIENCIAAPI,
    ListaCatalogoDEFICIENCIAJSONAPI,
    ListaCatalogoPROCEDIMIENTOJSONAPI,
    ListaCatalogoPROCEDIMIENTOAPI)

urlpatterns = [
    url(r'^catalogo/cie/lista_json/$',
        ListaCatalogoCIEJSONAPI.as_view()),

    url(r'^catalogo/cie/lista/$',
        ListaCatalogoCIEAPI.as_view()),

    url(r'^catalogo/deficiencia/lista_json/$',
        ListaCatalogoDEFICIENCIAJSONAPI.as_view()),

    url(r'^catalogo/deficiencia/lista/$',
        ListaCatalogoDEFICIENCIAAPI.as_view()),


    url(r'^catalogo/procedimiento/lista_json/$',
        ListaCatalogoPROCEDIMIENTOJSONAPI.as_view()),

    url(r'^catalogo/procedimiento/lista/$',
        ListaCatalogoPROCEDIMIENTOAPI.as_view()),


    # url(r'^catalogo/cie/detalle/(?P<id_ciex>\w+)/$',
    #     DetalleCatalogoCIEAPI.as_view()),
    # url(r'^catalogo/procedimiento/lista/$',
    #     ListaCatalogoProcedimientoAPI.as_view()),
    # url(r'^catalogo/procedimiento/detalle/(?P<codigo_cpt>\w+)/$',
    #     DetalleCatalogoProcedimientoAPI.as_view()),
    # url(r'^catalogo/deficiencia/lista/$',
    #     ListaCatalogoDeficienciaAPI.as_view()),
    # url(
    #     r'^catalogo/deficiencia/detalle/(?P<categoria_deficiencia>[a-zA-Z0-9.]+)/$',
    #     DetalleCatalogoDeficienciaAPI.as_view()),
    # url(r'^catalogo/discapacidad/lista/$',
    #     ListaCatalogoDiscapacidadAPI.as_view()),
    # url(r'^catalogo/discapacidad/detalle/(?P<categoria_discapacidad>\w+)/$',
    #     DetalleCatalogoDiscapacidadAPI.as_view()),
    # url(r'^catalogo/raza/lista/$', ListaCatalogoRazaAPI.as_view()),
    # url(r'^catalogo/raza/detalle/(?P<pk>\d+)/$',
    #     DetalleCatalogoRazaAPI.as_view()),
    # url(r'^catalogo/etnia/lista/$', ListaCatalogoEtniaAPI.as_view()),
    # url(r'^catalogo/etnia/detalle/(?P<id_etnia>\w+)/$',
    #     DetalleCatalogoEtniaAPI.as_view()),
    # url(r'^catalogo/financiador/lista/$',
    #     ListaCatalogoFinanciadorAPI.as_view()),
    # url(r'^catalogo/financiador/detalle/(?P<codigo>\w+)/$',
    #     DetalleCatalogoFinanciadorAPI.as_view()),
    # url(r'^catalogo/ayudatecnica/lista/$',
    #     ListaCatalogoAyudaTecnicaAPI.as_view()),
    # url(r'^catalogo/ayudatecnica/detalle/(?P<codigo>\w+)/$',
    #     DetalleCatalogoAyudaTecnicaAPI.as_view()),
    # url(r'^catalogo/gradoinstruccion/lista/$',
    #     ListaCatalogoGradoInstruccionAPI.as_view()),
    # url(r'^catalogo/gradoinstruccion/detalle/(?P<codigo>\w+)/$',
    #     DetalleCatalogoGradoInstruccionAPI.as_view()),
]

from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^establecimiento/lista_json/$',
        views.ListaEstablecimientoJSONAPI.as_view()),

    url(r'^establecimiento/lista/$',
        views.ListaEstablecmientoAPI.as_view()),

]

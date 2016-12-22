from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^consulta/(?P<num_dni>\d+)/$',
        views.consultadni,
        name='search_dni'),

]

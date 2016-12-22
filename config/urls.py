from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('discapacitado.users.urls', namespace='auth')),
    url(r'^', include('discapacitado.dnireniec.urls', namespace='reniec')),
    url(r'^', include('discapacitado.paciente.urls', namespace='paciente-app')),


    url(r'^api/v1/', include('discapacitado.catalogo.api.urls',
                             namespace='api-catalogo')),
    url(r'^api/v1/', include('discapacitado.paciente.api.urls',
                             namespace='api-paciente')),
    url(r'^api/v1/', include('discapacitado.establecimiento.api.urls',
                             namespace='api-establecimiento')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

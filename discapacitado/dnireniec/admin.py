from django.contrib import admin

from .forms import ServiceReniecForm
from .models import ServicioReniec


class ServicioReniecAdmin(admin.ModelAdmin):
    form = ServiceReniecForm


admin.site.register(ServicioReniec, ServicioReniecAdmin)

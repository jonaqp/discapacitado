from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import (
    User, UserEstablecimiento, UserCupo, UserDisponibilidad)


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


class MyUserCreationForm(UserCreationForm):
    error_message = UserCreationForm.error_messages.update({
        'duplicate_username': 'This username has already been taken.'
    })

    class Meta(UserCreationForm.Meta):
        model = User

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])


@admin.register(User)
class MyUserAdmin(AuthUserAdmin):
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    fieldsets = (
                    ('User Profile', {'fields': ('name',)}),
                ) + AuthUserAdmin.fieldsets
    list_display = ('username', 'is_superuser', 'get_groups')
    search_fields = ['username', 'name']


@admin.register(UserEstablecimiento)
class UserEstablishmentAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'get_usuario_establecimiento_lista',)


@admin.register(UserCupo)
class UserCuposAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'fecha', 'cupo',)


@admin.register(UserDisponibilidad)
class UserDisponibilidadAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'turno', 'horario',)

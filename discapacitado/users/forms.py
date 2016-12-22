from django import forms
from django.contrib.auth import get_user_model

from .models import UserEstablecimiento

User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField(label='Usuario')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username and not User.objects.filter(username=username).exists():
            raise forms.ValidationError('El usuario no existe')
        return username

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['autofocus'] = 'autofocus'


class UserEstablishmentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        initial = kwargs.get('initial', None)
        if initial:
            user = initial["user"]
            self.fields['establecimiento'].queryset = \
                UserEstablecimiento.objects.filter(
                    usuario=user
                ).values_list("establecimiento", flat=True)

    class Meta:
        model = UserEstablecimiento
        fields = ["establecimiento"]
        widgets = {
            'establecimiento': forms.Select(),
        }

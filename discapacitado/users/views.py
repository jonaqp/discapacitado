from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.views.generic import FormView, RedirectView

from . import forms


class LoginView(FormView):

    template_name = 'users/login.html'
    form_class = forms.LoginForm

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user:
            login(self.request, user)
            return super().form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        next = self.request.GET.get('next')
        if next is not None:
            return next
        return '/establecimiento'


class LogoutView(RedirectView):

    def get_redirect_url(self, **kwargs):
        logout(self.request)
        self.request.session.flush()
        return '/'

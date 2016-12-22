from django.test import RequestFactory, TestCase
from importlib import import_module

from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import resolve

from .. import views


User = get_user_model()


def create_active_user():
    user = User(username='test', email='test@test.com')
    user.set_password('secret')
    user.save()
    return user


class LoginViewTestCase(TestCase):

    def setUp(self):
        self.view = views.LoginView.as_view()
        self.session_engine = import_module(settings.SESSION_ENGINE)

    def test_match_expected_view(self):
        url = resolve('/login/')
        self.assertEqual(url.func.__name__, self.view.__name__)

    def test_load_sucessful(self):
        factory = RequestFactory()
        request = factory.get('/')
        response = self.view(request)
        self.assertEqual(response.status_code, 200)

    def test_login_success(self):
        factory = RequestFactory()
        user = create_active_user()
        request = factory.post('/', {
            'username': user.username,
            'password': 'secret'
        })
        request.session = self.session_engine.SessionStore('secret')
        response = self.view(request)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

    def test_login_redirect_to_next_url(self):
        factory = RequestFactory()
        user = create_active_user()
        request = factory.post('/?next=/another-url/', {
            'username': user.username,
            'password': 'secret'
        })
        request.session = self.session_engine.SessionStore('secret')
        response = self.view(request)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/another-url/')

    def test_login_error_username_not_found(self):
        """The username does not found in db"""
        factory = RequestFactory()
        create_active_user()
        request = factory.post('/', {
            'username': 'anotherusername',
            'password': 'test'
        })
        request.session = self.session_engine.SessionStore('secret')
        response = self.view(request)
        self.assertIn('username', response.context_data['form'].errors)
        self.assertEqual(response.status_code, 200)

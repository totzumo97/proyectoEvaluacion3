from django.test import TestCase
from blog.models import Post
from users.forms import UserRegisterForm
from django.contrib.auth.models import AnonymousUser, User

class UserFormCase(TestCase):
        
    def test_valid_form(self):
        data = {'username': 'Testuser', 'email': 'test@gmail.com','password1': 'testing321', 'password2': 'testing321', }
        form = UserRegisterForm(data=data)
        self.assertTrue(form.is_valid())
        
    def test_invalid_form(self):
        data = {'username': '', 'email': '','password1': 'testing321', 'password2': 'testing321', }
        form = UserRegisterForm(data=data)
        self.assertFalse(form.is_valid())

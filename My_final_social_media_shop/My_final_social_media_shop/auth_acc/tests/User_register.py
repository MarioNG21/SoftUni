from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from My_final_social_media_shop.auth_acc.forms import CreationUser
from My_final_social_media_shop.auth_acc.models import Profile

UserModel = get_user_model()


class AppUserTest(TestCase):
    VALID_USER_CREDENTIALS = {
        'email': 'test21@gmail.com',
        'password': '123qwe123',
    }

    VALID_PROFILE_CREDENTIALS = {
        'first_name': 'Test',
        'last_name': 'Testov',
        'age': 15,
        'gender': Profile.MALE,
    }

    def test_register_load_template(self):
        request = self.client.get(reverse('register user'))

        self.assertTemplateUsed('auth/registration.html')

    def test_register_form_valid__should_create_user(self):
        data = {
            **self.VALID_PROFILE_CREDENTIALS,
            'email': 'test2@gmail.com',
            'password1': 'qwe123qwexzxzxzxz',
            'password2': 'qwe123qwexzxzxzxz',
        }

        request = self.client.post(reverse('register user'), data=data)

        actual_content_to_check = request.context.dicts[1]
        user = actual_content_to_check['user']

        expected_token = actual_content_to_check['token']
        expected_uid = actual_content_to_check['uid']

        uid = urlsafe_base64_encode(force_bytes(user.pk)),
        token = default_token_generator.make_token(user)

        redirect_after_email_is_sent = reverse(
            'login user') + f'?command=verification&email={user.email}'

        self.assertEqual(expected_token, token)
        self.assertEqual(expected_uid, uid[0])

        self.assertRedirects(request, redirect_after_email_is_sent, 302)


def test_register_form_invalid_should_not_create_profile(self):
    pass


def test_register_form_is_valid__should_send_mail_after_creating_profile(self):
    pass

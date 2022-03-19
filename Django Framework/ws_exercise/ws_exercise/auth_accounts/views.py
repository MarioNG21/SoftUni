from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import forms as auth_forms, get_user_model
from django.contrib.auth import views as auth_views

from ws_exercise.petstagram.forms import ProfileCreateForm

UserModel = get_user_model()


class UserRegistrationForm(auth_forms.UserCreationForm, ProfileCreateForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = UserModel
        fields = ['username', 'password1', 'password2']
        labels = {
            'username': 'Enter username',
            'password1': 'Enter password',
            'password2': 'Enter password again'
        }


class CreateProfileView(views.CreateView):
    template_name = 'part2/profile_create.html'
    success_url = reverse_lazy('home')
    form_class = UserRegistrationForm


class UserLoginView(auth_views.LoginView):
    template_name = 'auth_pages/login_page.html'
    success_url = reverse_lazy('dashboard')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()

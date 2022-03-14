from django.shortcuts import render
from django.contrib.auth import views as auth_views, get_user_model, login
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import forms as auth_forms

UserModel = get_user_model()


class UserRegistrationForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('email',)


class UserRegistrationView(views.CreateView):
    form_class = UserRegistrationForm
    template_name = 'auth/registration.html'
    success_url = reverse_lazy('login user')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class UserLoginView(auth_views.LoginView):
    template_name = 'auth/login.html'
    model = UserModel
    success_url = reverse_lazy('')


class UserLogoutView(auth_views.LogoutView):
    pass

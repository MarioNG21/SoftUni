from django import forms

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import forms as auth_forms, get_user_model
from django.contrib.auth import views as auth_views

from ws_exercise.auth_accounts.forms import ProfileCreateForm
from ws_exercise.auth_accounts.models import Profile

from ws_exercise.petstagram.models import Pet, PetPhoto

UserModel = get_user_model()


class UserRegistrationForm(auth_forms.UserCreationForm, ProfileCreateForm):
    MAX_LENGTH_NAME = 30
    MALE = 'Male'
    FEMALE = 'Female'
    DO_NOT_SHOW = 'Do not show'
    GENDER = [(x, x) for x in (MALE, FEMALE, DO_NOT_SHOW)]

    first_name = forms.CharField(
        max_length=MAX_LENGTH_NAME,


    )

    last_name = forms.CharField(
        max_length=MAX_LENGTH_NAME,

    )

    profile_picture = forms.URLField()

    date_of_birth = forms.DateField(

    )

    description = forms.Textarea(

    )

    email = forms.EmailField(

    )

    gender = forms.ChoiceField(

        choices=GENDER
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = UserModel
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'profile_picture', 'email',
                  'date_of_birth', 'gender']
        labels = {
            'username': 'Enter username',
            'password1': 'Enter password',
            'password2': 'Enter password again',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'profile_picture': 'Link to Profile Picture'
        }

        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'First Name'
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Last Name'
            }),
            'profile_picture': forms.URLInput(attrs={
                'placeholder': 'Enter URL'
            }),
            'username': forms.TextInput(attrs={
                'placeholder': 'Enter username'
            }),
            'password1': forms.TextInput(attrs={
                'placeholder': 'Enter password'
            }),
            'password2': forms.TextInput(attrs={
                'placeholder': 'Enter password again'
            }),
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


class ProfileView(views.DetailView):
    model = Profile
    template_name = 'profile_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pets'] = Pet.objects.filter(user_id=self.object.user_id)
        context['count'] = PetPhoto.objects.filter(user=self.request.user).distinct().count()
        context['likes'] = sum(x.likes for x in PetPhoto.objects.filter(user=self.request.user).distinct())
        return context

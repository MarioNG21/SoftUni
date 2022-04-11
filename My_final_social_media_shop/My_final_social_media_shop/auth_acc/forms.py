import os

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth import forms as auth_forms
from django.core.exceptions import ValidationError

from My_final_social_media_shop.auth_acc.models import Profile
from My_final_social_media_shop.auth_acc.validators import age_validate

UserModel = get_user_model()


class CreationUser(auth_forms.UserCreationForm):
    first_name = forms.CharField(
        max_length=Profile.FIRST_NAME_LENGTH,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your first name here'}),
        label='First Name'
    )
    last_name = forms.CharField(
        max_length=Profile.LAST_NAME_LENGTH,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your last name here'}),
        label='Last Name'
    )
    age = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter your age here'})
        , validators=(age_validate,))
    gender = forms.ChoiceField(
        choices=Profile.CHOICES
    )

    def save(self, commit=True):
        return super().save(commit=commit)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

        self.fields['password1'].widget = forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter your password here'})
        self.fields['password2'].widget = forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter the same password here'})

    class Meta:
        model = UserModel
        fields = ('email', 'password1', 'password2', 'first_name', 'last_name', 'age', 'gender')
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email address here'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Enter your password here'})
        }


class UserChangePasswordForm(auth_forms.PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = UserModel
        fields = '__all__'


class ForgotPasswordForm(forms.Form):
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

        self.fields['email'].widget = forms.EmailInput(attrs={
            'placeholder': 'Enter your Email address'
        })


class CreateProfileForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.user = user
        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def save(self, commit=True):
        obj = super().save(commit=False)
        obj.user = self.user
        if commit:
            obj.save()

        return obj

    class Meta:
        model = Profile
        exclude = ('user',)
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter your first name here'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter your last name here'}),
            'age': forms.NumberInput(attrs={'placeholder': 'Enter your age here'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Enter your phone here'}),

        }

        labels = {
            'firs_name': 'First Name',
            'last_name': 'Last Name',
            'profile_picture': 'Profile Picture',

        }


class ProfileUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Profile
        exclude = ('user',)
        widgets = {

            'phone': forms.TextInput(attrs={'placeholder': 'Enter your phone number if you want to have one'}),

        }


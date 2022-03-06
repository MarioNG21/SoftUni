from datetime import date

from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator

from workshop1.petstagram.models import Profile, Pet
from workshop1.petstagram.validators import validation_year_in_range, validate_only_letters


# class ProfileForm(forms.ModelForm):
#   class Meta:
#         model = Profile
#         fields = ('first_name', 'last_name', 'profile_picture')
#         widgets = {
#             'first_name': forms.TextInput(attrs={
# 'class': 'form-control',
#                 'placeholder': 'Enter first name'
#             }),
#             'last_name': forms.TextInput(attrs={
# 'class': 'form-control',
#                 'placeholder': 'Enter last name'
#             }),
#             'profile_picture': forms.URLInput(attrs={
# 'class': 'form-control',
#                 'placeholder': 'Enter first name'
#             }),
#
#
# }

class ProfileForm(forms.Form):
    first_name = forms.CharField(
        max_length=30,
        required=True,
        validators=(MinLengthValidator(2), validate_only_letters),
        widget=(
            forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter first name'
            })
        )
    )

    last_name = forms.CharField(max_length=30,
                                required=True,
                                validators=(MinLengthValidator(2), validate_only_letters),
                                widget=(
                                    forms.TextInput(attrs={
                                        'class': 'form-control',
                                        'placeholder': 'Enter first name'
                                    })
                                )
                                )

    profile_picture = forms.URLField(
        required=True,
        widget=(
            forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter URL'
            })

        )

    )


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter first name'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter last name'
                }
            ),
            'picture': forms.URLInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter URL'
                }
            ),
            'e_mail': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter email'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter description',
                    'rows': 3
                }
            ),
            'date_of_birth': forms.DateInput(attrs={
                'min': '1920-01-01',
                'class': 'form-control',
            }),
            'gender': forms.Select(
                choices=Profile.GENDER,

            )
        }


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ('name', 'type', 'date_of_birth')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter pet name',
            }),
        }


class EditPetForm(forms.ModelForm):
    MIN_DATE_OF_BIRTH = date(1920, 1, 1)
    MAX_DATE_OF_BIRTH = date.today()

    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data['date_of_birth']
        if date_of_birth < self.MIN_DATE_OF_BIRTH or date_of_birth > self.MAX_DATE_OF_BIRTH:
            raise ValidationError(
                f"Date of birth must be between {self.MIN_DATE_OF_BIRTH} and {self.MAX_DATE_OF_BIRTH}")
        return self.cleaned_data

    class Meta:
        model = Pet
        fields = ('name', 'type', 'date_of_birth')
        widgets = {
            'name': forms.TextInput(attrs={

                'class': 'form-control',
            }),
            'type': forms.Select(
                choices=Pet.CHOICES, attrs={
                    'class': 'form-control',
                }
            ),
            'date_of_birth': forms.SelectDateWidget(attrs={
                'class': 'form-control'
            })
        }
        labels = {
            'name': 'Pet Name'
        }


class DeletePetForm(forms.ModelForm):
    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Pet
        exclude = ('user_profile',)
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'disabled': 'disabled'
            }),
            'type': forms.Select(
                choices=Pet.CHOICES, attrs={
                    'class': 'form-control',
                    'disabled': 'disabled'
                }
            ),
            'date_of_birth': forms.SelectDateWidget(attrs={
                'class': 'form-control',
                'disabled': 'disabled'
            })
        }
        labels = {
            'name': 'Pet Name'
        }

from datetime import datetime

from django import forms

from ws_exercise.auth_accounts.models import Profile
from ws_exercise.petstagram.models import PetPhoto


class ProfileCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'profile_picture']

        labels = {
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
            })
        }


class ProfileEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'date_of_birth', 'email', 'gender', 'description')
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'profile_picture': 'Link to Profile Picture',
            'date_of_birth': 'Date of Birth',
            'email': 'Email',

        }

        widgets = {

            'description': forms.Textarea(attrs={
                'placeholder': 'Enter description',
                'rows': 3
            }
            ),
            'date_of_birth': forms.SelectDateWidget(years=[y for y in range(1920, datetime.today().year + 1)]),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter email'
            }),
            'gender': forms.Select(attrs={
                'placeholder': 'Do not show'
            })
        }


class DeleteForm(forms.ModelForm):
    def save(self, commit=True):
        pets = list(self.instance.pet_set.all())
        PetPhoto.objects.filter(tagged_pets=pets).delete()
        self.instance.delete()
        return self.instance

    class Meta:
        model = Profile
        exclude = '__all__'

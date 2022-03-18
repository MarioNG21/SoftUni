from datetime import datetime

from django import forms
from django.contrib.auth import get_user_model

from ws_exercise.petstagram.models import Profile, Pet, PetPhoto

UserModel = get_user_model()


class ProfileCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'profile_picture')
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
    class Meta:
        model = Profile
        exclude = '__all__'


class AddPetForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, fields in self.fields.items():
            fields.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Pet
        fields = ('name', 'type', 'date_of_birth')
        labels = {
            'name': 'Pet name',
            'type': 'Type',
            'date_of_birth': "Day of Birth"
        }

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter Pet Name'
            }),
            'type': forms.Select(),
            'date_of_birth': forms.SelectDateWidget(years=[y for y in range(1920, datetime.today().year + 1)])
        }


class PetEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, fields in self.fields.items():
            fields.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Pet
        fields = ('name', 'type', 'date_of_birth')
        widgets = {
            'date_of_birth': forms.SelectDateWidget(years=[y for y in range(1920, datetime.today().year + 1)])
        }


class PetDeleteForm(forms.ModelForm):
    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    class Meta:
        model = Pet
        fields = ('name', 'type', 'date_of_birth')
        widgets = {
            'date_of_birth': forms.SelectDateWidget()
        }


class AddPhotoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, fields in self.fields.items():
            fields.widget.attrs['class'] = 'form-control'

    class Meta:
        model = PetPhoto
        fields = ('photo', 'description', 'tagged_pets')
        labels = {
            'photo': 'Pet Image',
            'tagged_pets': 'Tag Pets'
        }

        widgets = {
            'photo': forms.FileInput(),
            'description': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Enter Description'
            }),

        }


class EditPhoto(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, fields in self.fields.items():
            fields.widget.attrs['class'] = 'form-control'

    class Meta:
        model = PetPhoto
        fields = ('description', 'tagged_pets')
        widgets = {
            'tagged_pets': forms.Select()
        }

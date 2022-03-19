from datetime import datetime

from django import forms
from django.contrib.auth import get_user_model

from ws_exercise.petstagram.models import Pet, PetPhoto

UserModel = get_user_model()


class AddPetForm(forms.ModelForm):

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        for _, fields in self.fields.items():
            fields.widget.attrs['class'] = 'form-control'

    def save(self, commit=True):
        result = super().save(commit=False)
        result.user = self.user
        if commit:
            result.save()
        return result

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
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        for _, fields in self.fields.items():
            fields.widget.attrs['class'] = 'form-control'

    def save(self, commit=True):
        result = super().save(commit=False)
        result.user = self.user
        if commit:
            result.save()

        return result

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
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

        for _, fields in self.fields.items():
            fields.widget.attrs['class'] = 'form-control'

    def save(self, commit=True):
        result = super().save(commit=False)
        result.user = self.user

    class Meta:
        model = PetPhoto
        fields = ('description', 'tagged_pets')
        widgets = {
            'tagged_pets': forms.Select()
        }

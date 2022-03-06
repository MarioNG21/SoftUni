from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator

from exam_main.music_app.models import username_valid_name, Album, Profile


def positive_age(value):
    if value < 0:
        raise ValidationError('Age must be positive')


class ProfileRegisterForm(forms.Form):
    username = forms.CharField(
        max_length=15,
        validators=(MinLengthValidator(2),
                    username_valid_name),
        widget=forms.TextInput(attrs={
            'placeholder': 'Username',
            'required': True
        })
    )
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Email',
        'required': True
    }))

    age = forms.IntegerField(
        validators=(positive_age,),
        widget=forms.NumberInput(attrs={
            'placeholder': 'Age'}),
        required=False)


class AddAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        widgets = {
            'album_name': forms.TextInput(attrs={'placeholder': 'Album Name'}),
            'artist': forms.TextInput(attrs={'placeholder': 'Artist'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description'}),
            'image_url': forms.URLInput(attrs={'placeholder': 'Image URL'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Price'})

        }
        labels = {
            'album_name': 'Album Name',
            'image_url': 'Image URL'
        }


class AlbumEditForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        labels = {
            'album_name': 'Album Name',
            'image_url': 'Image URL'
        }


class AlbumDeleteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Album
        fields = '__all__'
        labels = {
            'album_name': 'Album Name',
            'image_url': 'Image URL'
        }


class ProfileDeleteForm(forms.ModelForm):
    def save(self, commit=True):
        self.instance.delete()
        Album.objects.all().delete()
        return self.instance

    class Meta:
        model = Profile
        fields = ()

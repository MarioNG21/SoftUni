from django import forms

from exam_3.library.models import Profile, Book


class CreateProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.label_suffix = ''

    class Meta:
        model = Profile
        fields = '__all__'
        labels = {
            'image_url': 'Image URL',
            'first_name': 'First Name',
            'last_name': 'Last Name',
        }

        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'First Name'
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Last Name'
            }),
            'image_url': forms.URLInput(attrs={
                'placeholder': 'URL'
            })
        }


class EditProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.label_suffix = ''

    class Meta:
        model = Profile
        fields = '__all__'
        labels = {
            'image_url': 'Image URL',
            'first_name': 'First Name',
            'last_name': 'Last Name',
        }


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        self.instance.delete()
        Book.objects.all().delete()
        return self.instance

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.label_suffix = ''
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    class Meta:
        model = Profile
        fields = '__all__'
        labels = {
            'image_url': 'Image URL',
            'first_name': 'First Name',
            'last_name': 'Last Name',
        }


class AddBookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.label_suffix = ''

    class Meta:
        model = Book
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Title'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Description'
            }),
            'image': forms.URLInput(attrs={
                'placeholder': 'URL'
            }),
            'type': forms.TextInput(attrs={
                'placeholder': 'Fiction, Novel, Crime...'
            })
        }


class EditBook(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.label_suffix = ''

    class Meta:
        model = Book
        fields = '__all__'

from django import forms

from exam2.notes.models import Profile, Note


class CreateProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.label_suffix = ''

    class Meta:
        model = Profile
        fields = '__all__'
        labels = {
            'image_url': 'Link to Profile Image',
            'first_name': 'First Name',
            'last_name': 'Last Name,'
        }


class CreateNoteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.label_suffix = ''

    class Meta:
        model = Note
        fields = ('title', 'content', 'image_url')
        labels = {
            'image_url': 'Link to Image'
        }


class EditNoteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.label_suffix = ''

    class Meta:
        model = Note
        fields = '__all__'
        labels = {
            'image_url': 'Link to Image'
        }


class DeleteNoteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False
            field.label_suffix = ''

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Note
        fields = '__all__'
        labels = {
            'image_url': 'Link to Image'
        }


class DeleteProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False
            field.label_suffix = ''

    def save(self, commit=True):
        self.instance.delete()
        Note.objects.all().delete()
        return self.instance

    class Meta:
        model = Profile
        fields = '__all__'
        labels = {
            'image_url': 'Link to Profile Image'
        }

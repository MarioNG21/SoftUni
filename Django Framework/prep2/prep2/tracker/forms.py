import os

from django import forms

from prep2.tracker.models import Profile, Expense


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('budget', 'first_name', 'last_name', 'profile_image')
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'profile_image': 'Profile Image'
        }

        widgets = {
            'profile_image': forms.FileInput(attrs={
                'class': 'form-file'
            })
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('budget', 'first_name', 'last_name', 'profile_image')
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'profile_image': 'Profile Image'
        }

        widgets = {
            'profile_image': forms.FileInput(attrs={
                'class': 'form-file'
            })
        }


class DeleteProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        image = self.instance.profile_image.path
        self.instance.delete()
        Expense.objects.all().delete()
        os.remove(image)
        return self.instance

    class Meta:
        model = Profile
        fields = ()


class ExpenseCreateForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('title', 'description', 'expense_image', 'price')
        labels = {
            'expense_image': 'Link to Image'
        }


class ExpenseEditForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('title', 'description', 'expense_image', 'price')
        labels = {
            'expense_image': 'Link to Image'
        }


class ExpenseDeleteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Expense
        fields = ('title', 'description', 'expense_image', 'price')
        labels = {
            'expense_image': 'Link to Image'
        }

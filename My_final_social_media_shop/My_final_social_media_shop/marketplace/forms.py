from django import forms
from django_countries.widgets import CountrySelectWidget

from My_final_social_media_shop.marketplace.models import Product, Order, BillingAddress, Category


class CategoryAddForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Category
        fields = '__all__'


class CategoryEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Category
        fields = '__all__'


class CategoryDeleteForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ()


class CreationAdForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def save(self, commit=True):
        obj = super().save(commit=False)
        obj.user = self.user
        if commit:
            obj.save()
        return obj

    class Meta:
        model = Product
        exclude = ('upload_date', 'slug', 'user', 'thumbnail')

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Enter the name of your product here !'
                }
            ),
            'price': forms.NumberInput(
                attrs={
                    'placeholder': 'Enter the price here!'
                }
            ),

            'description': forms.Textarea(
                attrs={
                    'placeholder': "Enter meaningful description so the buyer has good perception of the item's condition"}
            )

        }


class EditAdForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Product
        exclude = ('user',)


class DeleteAdForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ()


class CheckOutForm(forms.ModelForm):

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
        model = BillingAddress
        exclude = ('user',)
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter your first name here'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter your last name here'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Enter your phone here'}),
            'address': forms.TextInput(attrs={'placeholder': 'Enter your address here'}),
            'state': forms.TextInput(attrs={'placeholder': 'Enter your state here'}),
            'zip': forms.TextInput(attrs={'placeholder': 'Enter your zip here'}),
            'country': CountrySelectWidget(attrs={'class': 'custom-select d-block w-100'}),

        }

        labels = {
            'firs_name': 'First Name',
            'last_name': 'Last Name',

        }


class PaymentForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def save(self, commit=True):
        obj = super().save(commit=False)
        obj.user = self.user
        if commit:
            obj.save()

        return obj

    class Meta:
        model = BillingAddress
        fields = ()

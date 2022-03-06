from django import forms


class CreateReviewForm(forms.Form):
    username = forms.CharField(max_length=40, label='User Name', error_messages={
        'required': 'Your name must not be empty!',
        'max_length': "Please enter short name!"
    })

    review_text = forms.CharField(label='Your Review', widget=forms.Textarea, max_length=500)
    rating = forms.IntegerField(label='Rating', min_value=1, max_value=5)

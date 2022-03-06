from django import forms

from FirstProject.youtube_project.models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'

    def clean(self):
        cleand_data = self.cleaned_data
        title = cleand_data.get('title')
        list_of_articles = Article.objects.filter(title__iexact=title) if Article.objects.filter(
            title__iexact=title) else None
        if list_of_articles:
            if title.lower() in list_of_articles[0].title:
                raise forms.ValidationError('This name is already used')
        return cleand_data

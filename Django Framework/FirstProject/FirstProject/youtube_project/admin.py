from django.contrib import admin

# Register your models here.
from FirstProject.youtube_project.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')
    list_edit = ('slug',)
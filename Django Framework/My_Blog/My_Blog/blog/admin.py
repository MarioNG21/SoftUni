from django.contrib import admin

# Register your models here.
from My_Blog.blog.models import Author, Post


class PostInLine(admin.StackedInline):
    model = Post


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    inlines = [PostInLine]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date', 'slug')
    prepopulated_fields = {
        'slug': ('title',)
    }

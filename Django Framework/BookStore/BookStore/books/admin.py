from django.contrib import admin
from django.utils.text import slugify

from BookStore.books.models import Author, Book


class BookInline(admin.StackedInline):
    model = Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('fist_name', 'last_name', 'age')
    inlines = (BookInline,)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'rating', 'slug')
    prepopulated_fields = {
        'slug': ('title',)
    }
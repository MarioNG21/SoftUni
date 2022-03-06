from django.contrib import admin


# Register your models here.
from exam1.recepie.models import Recipe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title',)

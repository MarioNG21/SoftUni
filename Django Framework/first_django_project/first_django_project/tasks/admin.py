from django.contrib import admin

from first_django_project.tasks.models import Task, Category


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_filter = ('title',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
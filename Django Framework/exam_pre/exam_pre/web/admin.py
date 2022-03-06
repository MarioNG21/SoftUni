from django.contrib import admin


# Register your models here.
from exam_pre.web.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'budget')

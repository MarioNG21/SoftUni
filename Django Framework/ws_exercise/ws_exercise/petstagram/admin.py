from django.contrib import admin

# Register your models here.
from ws_exercise.petstagram.models import Pet, PetPhoto


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'type')


@admin.register(PetPhoto)
class PetAdminAdmin(admin.ModelAdmin):
    list_display = ('photo', 'likes')

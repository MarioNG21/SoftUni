from django.contrib import admin

# Register your models here.
from workshop1.petstagram.models import Profile, Pet, PetPhoto


class PetInline(admin.StackedInline):
    model = Pet


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'profile_picture')
    inlines = (PetInline,)


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user_profile', 'type')


@admin.register(PetPhoto)
class PetPhotoAdmin(admin.ModelAdmin):
    pass

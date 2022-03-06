from django.contrib import admin

# Register your models here.
from obshtak_exercise.exercise_app.models import DoneExercise, Person


@admin.register(DoneExercise)
class ExerciseAppAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'egn')

from django.db import models


# Create your models here.

class DoneExercise(models.Model):
    Homework = 'Homework'
    Laundry = 'Laundry'
    Exercise = 'Exercise'
    Dishes = 'Dishes'

    name = models.CharField(
        max_length=20,
        unique=True,
        choices=(
            (Homework, Homework),
            (Laundry, Laundry),
            (Exercise, Exercise),
            (Dishes, Dishes)
        ),
        verbose_name='Chores'
    )

    def __str__(self):
        return f"This is your {self.name}"


class Person(models.Model):
    first_name = models.CharField(
        max_length=10,
        verbose_name="First Name",
    )

    last_name = models.CharField(
        max_length=20,
        verbose_name='Last Name',
    )

    egn = models.IntegerField(
        unique=True,
        verbose_name="EGN"
    )

    age = models.IntegerField()

    exercises = models.ManyToManyField(to=DoneExercise
    )
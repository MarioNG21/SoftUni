from django.db import models

# Create your models here.
from django.utils.text import slugify


class Address(models.Model):
    street = models.CharField(max_length=30)
    city = models.CharField(max_length=15)


class Author(models.Model):
    fist_name = models.CharField(
        max_length=15
    )

    last_name = models.CharField(
        max_length=20
    )
    age = models.IntegerField()

    street = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)

    @property
    def full_name(self):
        return f"{self.fist_name}-{self.last_name}"

    def __str__(self):
        return self.full_name


class Book(models.Model):
    title = models.CharField(
        max_length=20,
    )

    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE
    )

    date_of_publish = models.DateField(
        auto_now_add=True,

    )

    rating = models.IntegerField()

    slug = models.SlugField(default='', null=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} is written by {self.author} with {self.rating}"


class Country(models.Model):
    name = models.CharField(max_length=30)
    code = models.IntegerField()
    published_books = models.ManyToManyField(Book)

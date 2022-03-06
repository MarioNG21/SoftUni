from django.db import models

# Create your models here.
from django.template.defaultfilters import slugify


class Author(models.Model):
    MAX_LENGTH = 30

    first_name = models.CharField(
        max_length=MAX_LENGTH
    )

    last_name = models.CharField(
        max_length=MAX_LENGTH
    )

    email = models.EmailField()

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Post(models.Model):
    title = models.CharField(
        max_length=30
    )
    excerpt = models.TextField()

    image = models.ImageField(upload_to='images/')

    date = models.DateField(
        auto_now=True
    )

    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True
    )

    content = models.TextField()

    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ('-date',)


class Tag(models.Model):
    caption = models.CharField(
        max_length=25
    )
    posts = models.ManyToManyField(
        Post
    )

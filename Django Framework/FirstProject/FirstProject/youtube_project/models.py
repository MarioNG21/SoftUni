import random
from sqlite3 import connect

from articles.engine import Article
from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify


@receiver(pre_save, sender=Article)
def my_callback(sender, **kwargs):
    sender.slug = slugify(sender.title)


def identify_new_slug(instance, save=False, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)
    qs = Article.objects.filter(slug=slug).exclude(id=instance.id)
    if qs.exists():
        slug = f'{slug}-{random.randint}'
        return identify_new_slug(instance, save=save, new_slug=slug)
    instance.slug = slug
    if save:
        instance.save()

    return instance


class ArticleQuerySet(models.QuerySet):
    def search(self, query=None):
        if query is None or query == '':
            return self.none()
        lookups = Q(title__icontains=query) | Q(content__icontains=query)
        return self.filter(lookups)


class ArticleManager(models.Manager):
    def get_queryset(self):
        return ArticleQuerySet(self.model, using=self._db)

    def search(self, query=None):
        return self.get_queryset().search(query)


class Article(models.Model):
    title = models.CharField(
        max_length=20
    )
    content = models.TextField()

    slug = models.SlugField(
        unique=True,
        null=True,
        blank=True,
    )
    objects = ArticleManager()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

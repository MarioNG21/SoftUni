from django.contrib.auth import get_user_model
from django.db import models

from My_final_social_media_shop.auth_acc.models import Profile


class Category(models.Model):
    pass


class Product(models.Model):
    MAX_TITLE_LENGTH = 100
    SLUG_MAX_LENGTH = 50

    title = models.CharField(
        max_length=100
    )

    slug = models.SlugField(
        max_length=SLUG_MAX_LENGTH,
        null=False,
        blank=True,
        unique=True
    )

    price = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    product_image = models.ImageField(
        upload_to='media/products/'
    )

    description = models.TextField()

    upload_date = models.DateField(
        auto_now_add=True
    )

    '''
    todo: Add thumbnail field -> should re watch youtube video about shopping cart
    '''


class OrderItem(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )


class Order(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )

    items = models.ManyToManyField(
        OrderItem
    )

    date_created_on = models.DateField(
        auto_now_add=True
    )

    date_send_on = models.DateField()

    ordered = models.BooleanField(
        default=False
    )

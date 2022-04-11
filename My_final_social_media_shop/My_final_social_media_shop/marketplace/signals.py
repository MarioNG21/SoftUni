import os

from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver
from django.utils.text import slugify

from My_final_social_media_shop.marketplace.models import Product

# May have Problem here !!! Should try in admin
from My_final_social_media_shop.marketplace.utils import random_char_generator


@receiver(post_delete, sender=Product)
def delete_post(instance, **kwargs):
    product = instance if instance else None
    if product is not None:
        product_picture = product.product_image
        os.remove(product_picture.path)

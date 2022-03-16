from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from My_final_social_media_shop.marketplace.models import Product


# May have Problem here !!! Should try in admin
@receiver(pre_save, sender=Product)
def slug_create(sender, **kwargs):
    sender.slug = slugify(sender.title)
    sender.save()
    return sender

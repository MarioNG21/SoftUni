import os
from django.db.models.signals import post_delete
from django.dispatch import receiver

from My_final_social_media_shop.auth_acc.models import Profile, AppUser
from My_final_social_media_shop.marketplace.models import Product, OrderItem, Order


@receiver(post_delete, sender=Profile)
def delete_user_with_items(instance, **kwargs):
    profile = instance if instance else None
    if profile is not None:

        profile_user = AppUser.objects.get(id=profile.pk)

        profile_items = Product.objects.filter(user=profile_user)
        profile_item_orders = OrderItem.objects.filter(user=profile_user)
        profile_orders = Order.objects.filter(user=profile_user)

        if profile_orders.exists():
            profile_orders.delete()
        if profile_item_orders.exists():
            profile_item_orders.delete()
        if profile_items.exists():
            profile_items.delete()

        os.remove(profile.profile_picture.path)

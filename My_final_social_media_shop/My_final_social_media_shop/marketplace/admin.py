from django.contrib import admin

# Register your models here.
from django.utils.text import slugify

from My_final_social_media_shop.marketplace.models import Product, OrderItem, Order, Category, BillingAddress


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'category', 'product_image', 'description')
    list_filter = ('title', 'price')
    list_display_links = ('title', 'description')


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'quantity')
    list_filter = ('quantity',)
    list_display_links = ('user', 'quantity',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'ordered', 'date_created_on')
    list_filter = ('user', 'date_created_on')
    list_display_links = ('user', 'date_created_on', 'ordered')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('name',)
    list_display_links = ('name', 'slug')


@admin.register(BillingAddress)
class BillingAddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'address',)
    list_filter = ('user', 'first_name')
    list_display_links = ('user', 'first_name', 'address')

from io import BytesIO
from PIL import Image
from django.contrib.auth import get_user_model
from django.core.files import File
from django.core.validators import RegexValidator
from django.db import models
from django.utils.text import slugify
from django_countries.fields import CountryField

from My_final_social_media_shop.auth_acc.models import Profile
from My_final_social_media_shop.marketplace.validators import MaxSizePhotoValidator

UserModel = get_user_model()


class BillingAddress(models.Model):
    FIRST_NAME_LENGTH = 40
    LAST_NAME_LENGTH = 40
    MAX_LENGTH_ADDRESS = 50
    MAX_LENGTH_STATE = 70
    MAX_LENGTH_ZIP = 70
    MAX_LENGTH_PHONE = 16

    first_name = models.CharField(
        max_length=FIRST_NAME_LENGTH
    )

    last_name = models.CharField(
        max_length=LAST_NAME_LENGTH
    )

    address = models.CharField(
        max_length=MAX_LENGTH_ADDRESS
    )

    country = CountryField(multiple=False)

    state = models.CharField(
        max_length=MAX_LENGTH_STATE
    )

    zip = models.CharField(
        max_length=MAX_LENGTH_ZIP
    )

    phone = models.CharField(
        max_length=MAX_LENGTH_PHONE,
        validators=(RegexValidator(r'^\+?(?P<phone>(\d{8,15}))$', message='You must enter a valid phone number'),)

    )

    user = models.ForeignKey(
        UserModel, on_delete=models.CASCADE
    )


class Category(models.Model):
    MAX_LENGTH_CATEGORY_NAME = 50

    name = models.CharField(
        max_length=MAX_LENGTH_CATEGORY_NAME,
        unique=True
    )

    slug = models.SlugField(
        unique=True,
        blank=True,
    )

    category_img = models.ImageField(
        upload_to='media/category/'
    )

    def __str__(self):
        return f'{self.name.capitalize()}'

    class Meta:
        verbose_name_plural = 'Categories'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Product(models.Model):
    MAX_TITLE_LENGTH = 100

    title = models.CharField(
        max_length=100
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
        upload_to='media/products/',
        validators=(MaxSizePhotoValidator(5),)
    )

    description = models.TextField()

    upload_date = models.DateField(
        auto_now_add=True
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )

    thumbnail = models.ImageField(upload_to='media/products/thumbnails/', blank=True)

    def creating_thumbnail(self):
        img = Image.open(self.product_image)
        size = (200, 200)

        img.convert('RGB')

        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)
        thumbnail = File(thumb_io, name=f"{self.title}.jpeg")

        return thumbnail

    def save(self, *args, **kwargs):
        if not self.thumbnail:
            self.thumbnail = self.creating_thumbnail()

        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class OrderItem(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    quantity = models.IntegerField(default=1)

    purchased = models.BooleanField(
        default=False
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.product.title} of {self.quantity}"


class Order(models.Model):
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )

    items = models.ManyToManyField(
        OrderItem
    )

    date_created_on = models.DateField(
        auto_now_add=True
    )

    date_send_on = models.DateField(
        null=True,
        blank=True,
    )

    ordered = models.BooleanField(
        default=False
    )
    billing_address = models.OneToOneField(
        BillingAddress, on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return f"Order #{self.pk} of {self.user}"

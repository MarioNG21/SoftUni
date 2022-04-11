import decimal
from datetime import date

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from My_final_social_media_shop.marketplace.models import OrderItem, Category, Product, Order

UserModel = get_user_model()


def create_user(VALID_USER_CREDENTIALS):
    user = UserModel.objects.create_user(**VALID_USER_CREDENTIALS)
    user.is_active = True
    user.save()
    return user


class CartTest(TestCase):
    __VALID_CATEGORY_CREDENTIALS = {
        'name': 'Jeans',
        'slug': 'jeans',
        'category_img': 'jeans.jpg',
    }
    __VALID_PRODUCT_CREDENTIALS = {
        'title': 'dunki',
        'price': 20.00,
        'product_image': 'gucci.jpg',
        'thumbnail': 'gucci.jpg',
        'description': 'dsadsadasd',
        'upload_date': date(1, 12, 1)
    }

    __VALID_USER_CREDENTIALS = {
        'email': 'test@abv.bg',
        'password': '123qwe123',
    }

    def test_context_data_if_we_have_total_tax_and_all_obj(self):
        user = create_user(self.__VALID_USER_CREDENTIALS)

        category = Category.objects.create(
            **self.__VALID_CATEGORY_CREDENTIALS
        )
        product = Product.objects.create(
            **self.__VALID_PRODUCT_CREDENTIALS,
            user=user,
            category=category
        )

        order_item = OrderItem.objects.create(
            product=product,
            user=user
        )
        order_item_qs = OrderItem.objects.all()
        total = 0
        qnt = 0

        for item in order_item_qs:
            qnt += item.quantity
            total += (item.product.price * item.quantity)

        tax = total * decimal.Decimal(
            0.02)  # because price is decimal-field

        self.client.force_login(user)
        request = self.client.get(reverse('cart'))

        self.assertEqual(request.context_data['object_list'].count(), order_item_qs.count())
        self.assertEqual(request.context_data['total'], total)
        self.assertEqual(request.context_data['qnt'], 1)
        self.assertEqual(request.context_data['tax'], tax)

    def test_correct_template(self):
        user = create_user(self.__VALID_USER_CREDENTIALS)
        self.client.force_login(user)

        url = reverse('cart')
        template = 'cart_detail.html'

        request = self.client.get(url)
        self.assertTemplateUsed(request, template)

    def test_adding_object_with_click_should_create_order_and_set_this_item_to_items(self):
        user = create_user(self.__VALID_USER_CREDENTIALS)

        category = Category.objects.create(
            **self.__VALID_CATEGORY_CREDENTIALS
        )
        product = Product.objects.create(
            **self.__VALID_PRODUCT_CREDENTIALS,
            user=user,
            category=category,
        )

        order_item = OrderItem.objects.create(
            product=product,
            user=user,
            purchased=False
        )

        order_qs = Order.objects.filter(
            user=user,
            ordered=False,
        )
        self.assertEqual(order_qs.count(), 0)

        order = Order.objects.create(
            user=user,
            date_created_on=date(1, 2, 10)

        )
        order.items.add(order_item)
        self.client.force_login(user)
        self.client.get(reverse('click to add object', kwargs={'pk': product.pk}))

    def test_adding_object_with_click_should_create_add_qnt_and_goes_up_with_one(self):
        user = create_user(self.__VALID_USER_CREDENTIALS)

        category = Category.objects.create(
            **self.__VALID_CATEGORY_CREDENTIALS
        )
        product = Product.objects.create(
            **self.__VALID_PRODUCT_CREDENTIALS,
            user=user,
            category=category,
        )

        order_item = OrderItem.objects.create(
            product=product,
            user=user,
            purchased=False
        )
        order = Order.objects.create(
            user=user,
            date_created_on=date(1, 2, 10)

        )
        order.items.add(order_item)
        self.client.get(reverse('click to add object', kwargs={'pk': product.pk}))
        order_qs = Order.objects.filter(
            user=user,
            ordered=False,
        )
        self.assertEqual(order_qs.count(), 1)
        if order_qs.exists():
            order = order_qs.get()
            if order.items.filter(product=product, purchased=False):
                order_item.quantity += 1

        self.client.force_login(user)

        self.assertEqual(order_item.quantity, 2)

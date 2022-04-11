from datetime import date

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from My_final_social_media_shop.marketplace.models import Category, Product

UserModel = get_user_model()


class MarketTest(TestCase):
    __VALID_TEMPLATE = 'marketplace.html'
    __CATEGORY = Category
    __VALID_URL = reverse('marketplace')

    __VALID_CATEGORY2_CREDENTIALS = {
        'name': 'shirts',
        'slug': 'shirts',
        'category_img': 'shirt.jpg',
    }

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

    __VALID_PRODUCT2_CREDENTIALS = {
        'title': 'dunki2',
        'price': 22.00,
        'product_image': 'zara.jpg',
        'thumbnail': 'zara.jpg',
        'description': 'dsadsadasd',
        'upload_date': date(2, 12, 1)
    }

    __VALID_USER_CREDENTIALS = {
        'email': 'test@abv.bg',
        'password': '123qwe123'
    }

    def test_correct_template_usage(self):
        request = self.client.get(self.__VALID_URL)
        self.assertTemplateUsed(request, self.__VALID_TEMPLATE)

    def _create_category(self):
        return Category.objects.create(**self.__VALID_CATEGORY_CREDENTIALS)

    def _create_category2(self):
        return Category.objects.create(**self.__VALID_CATEGORY2_CREDENTIALS)

    def _create_user(self):
        return UserModel.objects.create_user(**self.__VALID_USER_CREDENTIALS)

    def test_get_from_context_all_categories__should_return_qs_category(self):
        category = self._create_category()
        categories = self.__CATEGORY.objects.all()
        request = self.client.get(self.__VALID_URL)

        self.assertEqual(request.context_data['categories'].get(), categories.get())

    def test_slug_in_query_set_should_return_filtered_qs_with_only_this_category(self):
        user = self._create_user()
        category = self._create_category()
        category2 = self._create_category2()

        product = Product.objects.create(
            **self.__VALID_PRODUCT_CREDENTIALS,
            user=user,
            category=category
        )

        product.save()

        product2 = Product.objects.create(
            **self.__VALID_PRODUCT2_CREDENTIALS,
            user=user,
            category=category2
        )
        product2.save()

        request = self.client.get(reverse('marketplace category', kwargs={'slug': category.slug}))
        product_qs = Product.objects.filter(category__slug__icontains=category.slug)

        self.assertEqual(request.context_data['object_list'].count(), 1)

    def test_no_slug_in_query_set_should__return_normal_qs(self):
        user = self._create_user()
        category = self._create_category()
        product = Product.objects.create(
            **self.__VALID_PRODUCT_CREDENTIALS,
            user=user,
            category=category
        )

        product.save()

        product2 = Product.objects.create(
            **self.__VALID_PRODUCT2_CREDENTIALS,
            user=user,
            category=category
        )
        product2.save()

        request = self.client.get(self.__VALID_URL)
        product_qs = Product.objects.all()

        self.assertEqual(request.context_data['object_list'].count(), product_qs.count())
    
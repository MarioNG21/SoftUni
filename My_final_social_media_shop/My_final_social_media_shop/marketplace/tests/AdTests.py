from datetime import date

import category as category
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from My_final_social_media_shop.marketplace.forms import CreationAdForm, EditAdForm
from My_final_social_media_shop.marketplace.models import Category, Product

UserModel = get_user_model()


def create_user(VALID_USER_CREDENTIALS):
    user = UserModel.objects.create_user(**VALID_USER_CREDENTIALS)
    user.is_active = True
    user.save()
    return user


def create_category(VALID_CATEGORY_CREDENTIALS):
    return Category.objects.create(**VALID_CATEGORY_CREDENTIALS)


class AdCreationTest(TestCase):
    __VALID_URL = reverse('add advertisement')
    __VALID_TEMPLATE = 'create_ad.html'

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
        'password': '1X<ISRUkw+tuK',
        'email': 'testuser1@gmail.com'
    }

    __FORM = CreationAdForm

    def test_correct_template(self):
        user = create_user(self.__VALID_USER_CREDENTIALS)
        self.client.force_login(user)
        request = self.client.get(self.__VALID_URL)

        self.assertTemplateUsed(request, self.__VALID_TEMPLATE)

    def test_correct_template_when_user_not_login(self):
        user = create_user(self.__VALID_USER_CREDENTIALS)
        request = self.client.get(self.__VALID_URL)
        self.assertTemplateNotUsed(request, self.__VALID_TEMPLATE)
        self.assertEqual(request.status_code, 302)

    # def test_creating_successful_ad_through_form(self):
    #     user = self._create_user()
    #     category = create_category(self.__VALID_CATEGORY_CREDENTIALS)
    #
    #     product = Product.objects.create(
    #         **self.__VALID_PRODUCT_CREDENTIALS,
    #         user=user,
    #         category=category
    #     )
    #
    #     product.save()
    #     data = {
    #         'title': product.title,
    #         'price': product.price,
    #         'description': product.description,
    #         'product_image': 'gucci.jpg',
    #         'category': product.category.name,
    #         'user': user,
    #
    #     }
    #     self.client.force_login(user)
    #     request = self.client.post(self.__VALID_URL, data=data)
    #     print(request.context_data['form'].errors)
    #
    #     self.assertTrue(request.context_data['form'].is_valid())


class AdEditTest(TestCase):
    __VALID_URL_WHEN_NO_PK = reverse('marketplace')
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

        'email': 'test@gmail.com',
        'password': '123qwe123'

    }

    def test_redirecting_to_login_if_user_is_not_authenticated(self):
        category = create_category(self.__VALID_CATEGORY_CREDENTIALS)
        user = create_user(self.__VALID_USER_CREDENTIALS)
        product = Product.objects.create(
            **self.__VALID_PRODUCT_CREDENTIALS,
            user=user,
            category=category
        )

        data = {
            'title': product.title,
            'price': product.price,
            'description': product.description,
            'product_image': 'gucci.jpg',
            'category': product.category.name,
            'user': user,
        }

        request = self.client.get(reverse('edit advertisement', kwargs={'pk': product.pk}))
        self.assertRedirects(request, f"{reverse('login user')}?next=%2Fedit_ad%2F1%2F")

    def test_loading_correct_template_when_user_is_logged_in(self):
        category = create_category(self.__VALID_CATEGORY_CREDENTIALS)
        user = create_user(self.__VALID_USER_CREDENTIALS)
        product = Product.objects.create(
            **self.__VALID_PRODUCT_CREDENTIALS,
            user=user,
            category=category
        )
        self.client.force_login(user)
        data = {
            'title': product.title,
            'price': product.price,
            'description': product.description,
            'product_image': 'gucci.jpg',
            'category': product.category.name,
            'thumbnail': product.thumbnail,
            'user': user,
        }
        request = self.client.post(reverse('edit advertisement', kwargs={'pk': product.pk}), data=data)
        print(request.context_data['form'].errors)

    def test_redirect_to_detail_view_if_product_is_edited_successfully(self):
        pass

    def test_redirect_to_market_view_if_product_is_edited_unsuccessfully(self):
        pass

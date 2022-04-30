from django.urls import path

from CarAPI.cars.views import UserCarIndexAPI, UserCarUpdateAPIView, UserCarDeleteAPIView, CarBrandListCreateAPIView, \
    CarBrandUpdateAPIView, CarBrandDeleteAPIView, CarModelListCreateAPIView, CarModelUpdateAPIView, \
    CarModelDeleteAPIView

urlpatterns = (
    path('', UserCarIndexAPI.as_view(), name='home'),
    path('usercar_update/<int:pk>/', UserCarUpdateAPIView.as_view(), name='update user car'),
    path('usercar_delete/<int:pk>/', UserCarDeleteAPIView.as_view(), name='delete user car'),

    # # CAR BRAND
    path('car_brand/list_create/', CarBrandListCreateAPIView.as_view(), name='list car brands'),
    path('car_brand/update/<int:pk>/', CarBrandUpdateAPIView.as_view(), name='update car brand'),
    path('car_brand/delete/<int:pk>/', CarBrandDeleteAPIView.as_view(), name='delete car brand'),

    # # CAR MODEL
    path('car_model/list_create/', CarModelListCreateAPIView.as_view(), name='list car models'),
    path('car_model/update/<int:pk>/', CarModelUpdateAPIView.as_view(), name='update car model'),
    path('car_model/delete/<int:pk>/', CarModelDeleteAPIView.as_view(), name='delete car model')
)

from django.urls import path
from django.views.generic import TemplateView

from My_final_social_media_shop.auth_acc.views import UserRegistrationView, UserLoginView, UserLogoutView

urlpatterns = [
    path('', TemplateView.as_view(template_name='base/index.html'), name='index'),
    path('register/', UserRegistrationView.as_view(), name='register user'),
    path('login/', UserLoginView.as_view(), name='login user'),
    path('logout/', UserLogoutView.as_view(), name='logout user'),
]

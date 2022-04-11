from django.urls import path
from django.views.generic import TemplateView

from My_final_social_media_shop.auth_acc.views import UserRegistrationView, UserLoginView, UserLogoutView, \
    ActivationView, ForgotPasswordsView, UserChangePasswordView, UpdateProfileView, DeleteProfileView, CreateProfileView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register user'),
    path('login/', UserLoginView.as_view(), name='login user'),
    path('logout/', UserLogoutView.as_view(), name='logout user'),

    # Paths with email send
    path('forgot_password/', ForgotPasswordsView.as_view(), name='password-change'),
    path('activation/<uid>/<token>/', ActivationView.as_view(), name='activation'),
    path('reset_password/<uidb64>/<token>/', UserChangePasswordView.as_view(), name='reset_password'),

    path('create_profile/', CreateProfileView.as_view(), name='create profile'),
    path('profile/<int:pk>/', UpdateProfileView.as_view(), name='profile'),
    path('delete_profile/<int:pk>/', DeleteProfileView.as_view(), name='delete profile'),
]

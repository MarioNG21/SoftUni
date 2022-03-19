from django.urls import path

from ws_exercise.auth_accounts.views import CreateProfileView, UserLoginView, ProfileView


urlpatterns = [
    path('create-profile/', CreateProfileView.as_view(), name='create profile'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    #
    # path('profile/edit-profile/<int:pk>/', EditView, name='edit profile'),

    # path('edit-password/<int:pk>/', EditPasswprdView, name='edit password')
]

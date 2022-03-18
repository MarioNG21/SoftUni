
from django.urls import path

from ws_exercise.auth_accounts.views import CreateProfileView, UserLoginView

urlpatterns = [
    path('create-profile/', CreateProfileView.as_view(), name='create profile'),
    path('login/', UserLoginView.as_view(), name='login'),
    # path('profile/<int:pk>/', DetailsView, name='profile details'),
    # path('edit-profile/<int:pk>/', EditProfileView, name='edit profile'),
    # path('edit-password/<int:pk>/', EditPasswprdView, name='edit password')
]

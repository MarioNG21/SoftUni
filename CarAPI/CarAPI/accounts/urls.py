from django.urls import path

from CarAPI.accounts.views import UserListAPIView, RegisterAPIView, LoginAPIView

urlpatterns = (
    path('list_users/', UserListAPIView.as_view(), name='list-users'),
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login')
)

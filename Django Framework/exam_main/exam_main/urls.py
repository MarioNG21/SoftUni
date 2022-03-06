"""exam_main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from exam_main.music_app.views import home, add_album, details_album, edit_album, delete_album, profile_details, \
    delete_profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('album/add', add_album, name='add_album'),
    path('album/details/<int:pk>/', details_album, name='details'),
    path('album/edit/<int:pk>/', edit_album, name='edit'),
    path('album/delete/<int:pk>/', delete_album, name='delete'),

    path('profile/details/', profile_details, name='profile_details'),
    path('profile/delete/', delete_profile, name='delete_profile'),
]

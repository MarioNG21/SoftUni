"""workshop1 URL Configuration

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

from workshop1.petstagram.views.generic import show_home, show_dashboard
from workshop1.petstagram.views.pet import edit_pet, delete_pet, add_pet
from workshop1.petstagram.views.photos import edit_pet_photo, like_pet_photo, create_pet_photo, show_photo_details
from workshop1.petstagram.views.profile import show_profile, create_profile, edit_profile, delete_profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_home, name='home'),
    path('dashboard/', show_dashboard, name='dashboard'),

    path('profile/', show_profile, name='profile'),

    path('profile/create/', create_profile, name='create profile'),

    path('profile/edit//', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),

    path('photo/details/<int:pk>', show_photo_details, name='pet photo details'),
    path('photo/add/', create_pet_photo, name='create photo'),
    path('photo/edit/<int:pk>/', edit_pet_photo, name='edit pet photo'),
    path('photo/like/<int:pk>/', like_pet_photo, name='like pet photo'),
    path('pet/add/', add_pet, name='create pet'),
    path('pet/edit/<int:pk>/', edit_pet, name='edit pet'),
    path('pet/delete/<int:pk>/', delete_pet, name='delete pet'),

]

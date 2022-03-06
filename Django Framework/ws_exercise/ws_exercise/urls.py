"""ws_exercise URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from ws_exercise.petstagram.views import home, show_dashboard, show_profile, show_photo_details, photo_like, \
    create_profile, edit_profile, delete_profile, add_pet, edit_pet, delete_pet, add_photo, edit_photo

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', home, name='home'),

                  path('dashboard/', show_dashboard, name='dashboard'),

                  path('profile/', show_profile, name='profile'),
                  path('profile/create/', create_profile, name='create profile'),
                  path('profile/edit/', edit_profile, name='edit profile'),
                  path('profile/delete/', delete_profile, name='delete profile'),

                  path('pet/add/', add_pet, name='add pet'),
                  path('pet/edit/<int:pk>/', edit_pet, name='edit pet'),
                  path('pet/delete/<int:pk>', delete_pet, name='delete pet'),

                  path('photo/add/', add_photo, name='add photo'),
                  path('photo/edit/<int:pk>/', edit_photo, name='edit photo'),
                  path('photo/details/<int:id>/', show_photo_details, name='photo_details'),
                  path('photo/likes/<int:id>/', photo_like, name='like')

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""exam_3 URL Configuration

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

from exam_3.library.views import home, add_book, edit_book, details_book, show_profile, edit_profile, delete_profile, \
    delete_book

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),

    path('add/', add_book, name='add book'),
    path('edit/<int:id>/', edit_book, name='edit book'),
    path('details/<int:id>/', details_book, name='details book'),
    path('delete/<int:id>/', delete_book, name='delete book'),

    path('profile/', show_profile, name='profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile')
]

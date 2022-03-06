from django.urls import path

from first_django_project.tasks.views import home

urlpatterns = [
    path('', home)
]

from django.urls import path

from exam_pre.web.views import show_index, create_index, edit_expnses, delete_expnses, show_profile, create_profile, \
    edit_profile, delete_profile

urlpatterns = [
    path('', show_index, name='show index'),
    path('create/', create_index, name='create expnses'),
    path('edit/<int:pk>/', edit_expnses, name='edit expnses'),
    path('delete/<int:pk>/', delete_expnses, name='delete expnses'),

    path('profile/', show_profile, name='show profile'),
    path('profile/create/', create_profile, name='create profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete', delete_profile, name='delete profile'),
]

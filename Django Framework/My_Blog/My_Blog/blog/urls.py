from django.urls import path

from My_Blog.blog.views import post_detail, list_of_posts, starting_page

urlpatterns = [
    path('', starting_page, name='index'),
    path('posts/', list_of_posts, name='list of posts'),
    path('post/<slug:slug>', post_detail, name='post detail')
]

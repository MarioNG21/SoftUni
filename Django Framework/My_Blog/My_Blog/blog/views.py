from django.shortcuts import render
from datetime import date

from My_Blog.blog.models import Post


def starting_page(request):
    latest_posts = Post.objects.all().order_by('-date')[:3]

    context = {
        'posts': latest_posts
    }
    return render(request, 'index.html', context)


def list_of_posts(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'all_posts.html', context)


def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    context = {
        'post': post
    }
    return render(request, 'post_detail.html', context)

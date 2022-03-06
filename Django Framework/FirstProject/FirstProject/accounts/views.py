from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.

#

from django.urls import reverse_lazy

from FirstProject.youtube_project.models import Article


def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }

    return render(request, 'index.html', context)


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'login.html', context)


def logout_view(request):
    context = {}
    if request.method == "POST":
        logout(request)

        return redirect(reverse_lazy('login'))
    return render(request, 'logout.html', context)


def register_view(request):
    form = UserCreationForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        user_obj = form.save()
        context['user'] = user_obj
        return redirect(reverse_lazy('login'))

    return render(request, 'register.html', context)

from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def home_page(request):
    context = {
        'home': "This is our home page",
        'welcome': "Welcome to my first page",
    }
    return render(request, 'base/base.html', context)


def person_house(request, id):
    return HttpResponse(f"This is person {id} house")


def house(request):
    return redirect(to='')

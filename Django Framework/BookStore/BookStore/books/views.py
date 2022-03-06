from django.shortcuts import render

# Create your views here.
from BookStore.books.models import Author, Book


def index(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'index.html', context)


def book_details(request, slug):
    current_book = Book.objects.filter(slug=slug).get()
    context = {'book': current_book}
    return render(request, 'book_details.html', context)

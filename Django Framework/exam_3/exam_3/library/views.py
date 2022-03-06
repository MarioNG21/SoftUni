from django.shortcuts import render, redirect

# Create your views here.
from exam_3.library.forms import CreateProfileForm, AddBookForm, EditBook, EditProfileForm, DeleteProfileForm
from exam_3.library.models import Profile, Book


def get_books():
    books = Book.objects.all()
    if books:
        return books
    return None


def get_profile():
    profile = Profile.objects.all()
    if profile:
        return Profile.objects.get()
    return None


def home(request):
    profile = get_profile()
    books = get_books()
    if profile is None:
        return home_with_no_profile(request)
    context = {
        'profile': profile,
        'books': books
    }

    return render(request, 'home-with-profile.html', context)


def home_with_no_profile(request):
    if request.method == "POST":
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateProfileForm()

    context = {
        'form': form
    }
    return render(request, 'home-no-profile.html', context)


def add_book(request):
    profile = get_profile()
    if request.method == "POST":
        form = AddBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = AddBookForm()

    context = {
        'form': form,
        'profile': profile
    }
    return render(request, 'add-book.html', context)


def edit_book(request, id):
    book = get_books().get(pk=id)
    profile = get_profile()
    if request.method == "POST":
        form = EditBook(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EditBook(instance=book)

    context = {
        'form': form,
        'book': book,
        'profile': profile
    }

    return render(request, 'edit-book.html', context)


def details_book(request, id):
    books = get_books()
    profile = get_profile()
    current_book = books.get(pk=id)
    context = {
        'book': current_book,
        'profile': profile
    }

    return render(request, 'book-details.html', context)


def delete_book(request, id):
    books = get_books()
    book = books.get(pk=id)
    book.delete()
    return redirect('home')


def show_profile(request):
    profile = get_profile()
    context = {
        'profile': profile
    }

    return render(request, 'profile.html', context)


def edit_profile(request):
    profile = get_profile()
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EditProfileForm(instance=profile)

    context = {
        'form': form,
        'profile': profile
    }

    return render(request, 'edit-profile.html', context)


def delete_profile(request):
    profile = get_profile()
    if request.method == "POST":
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DeleteProfileForm(instance=profile)

    context = {
        'form': form,
        'profile': profile
    }

    return render(request, 'delete-profile.html', context)

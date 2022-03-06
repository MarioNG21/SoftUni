from django.shortcuts import render, redirect

from exam_main.music_app.forms import ProfileRegisterForm, AddAlbumForm, AlbumEditForm, AlbumDeleteForm, \
    ProfileDeleteForm
from exam_main.music_app.models import Profile, Album


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]

    return None


def home(request):
    profile = get_profile()
    albums = Album.objects.all()
    if profile is None:
        return home_no_profile(request)

    context = {
        'profile': profile,
        'albums': albums
    }
    return render(request, 'home-with-profile.html', context)


def home_no_profile(request):
    if request.method == 'POST':
        form = ProfileRegisterForm(request.POST)
        if form.is_valid():
            profile = Profile(**form.cleaned_data)
            profile.save()
            return redirect('home')

    else:
        form = ProfileRegisterForm()
    context = {
        'form': form,
        'has_no_profile': True
    }
    return render(request, 'home-no-profile.html', context)


def add_album(request):
    if request.method == "POST":
        form = AddAlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddAlbumForm()

    context = {
        'form': form
    }
    return render(request, 'add-album.html', context)


def details_album(request, pk):
    album = Album.objects.get(pk=pk)

    context = {
        'album': album
    }
    return render(request, 'album-details.html', context)


def edit_album(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == "POST":
        form = AlbumEditForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AlbumEditForm(instance=album)

    context = {
        'form': form,
        'album': album
    }

    return render(request, 'edit-album.html', context)


def delete_album(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        form = AlbumDeleteForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AlbumDeleteForm(instance=album)

    context = {
        'album': album,
        'form': form
    }

    return render(request, 'delete-album.html', context)


def profile_details(request):
    profile = get_profile()
    albums_count = Album.objects.all().count()
    context = {
        'profile': profile,
        'albums_count': albums_count
    }
    return render(request, 'profile-details.html', context)


def delete_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProfileDeleteForm(instance=profile)

    context = {
        'profile': profile,
        'form': form
    }
    return render(request, 'profile-delete.html', context)

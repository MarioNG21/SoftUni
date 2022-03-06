
from django.shortcuts import render, redirect
from exam2.notes.forms import CreateProfileForm, CreateNoteForm, EditNoteForm, DeleteNoteForm, DeleteProfileForm
from exam2.notes.models import Profile, Note


def get_notes():
    notes = Note.objects.all()
    if notes:
        return notes
    return None


def get_profile():
    profile = Profile.objects.all()
    if profile:
        return profile[0]
    else:
        return None


def home(request):
    profile = get_profile()
    if profile is None:
        return home_with_no_profile(request)

    notes = get_notes()

    context = {
        'profile': profile,
        'notes': notes

    }

    return render(request, 'home-with-profile.html', context)


def home_with_no_profile(request):
    if request.method == 'POST':
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


def add_note(request):
    if request.method == 'POST':
        form = CreateNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateNoteForm()

    context = {
        'form': form
    }
    return render(request, 'note-create.html', context)


def edit_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EditNoteForm(instance=note)

    context = {
        'form': form,
        'note': note
    }

    return render(request, 'note-edit.html', context)


def delete_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == "POST":
        form = DeleteNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = DeleteNoteForm(instance=note)

    context = {
        'form': form,
        'note': note
    }

    return render(request, 'note-delete.html', context)


def details_note(request, pk):
    note = Note.objects.get(pk=pk)
    context = {
        'note': note
    }
    return render(request, 'note-details.html', context)


def show_profile(request):
    profile = get_profile()
    notes = get_notes()
    context = {
        'profile': profile,
        'notes': notes
    }

    return render(request, 'profile.html', context)


def delete_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DeleteProfileForm(instance=profile)
    context = {
        'form': form
    }
    return render(request, 'profile-delete.html', context)
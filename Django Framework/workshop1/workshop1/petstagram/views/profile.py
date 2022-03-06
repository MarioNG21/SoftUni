from django.shortcuts import redirect, render

from workshop1.petstagram.forms.forms import ProfileForm, ProfileEditForm
from workshop1.petstagram.helpers import get_profile
from workshop1.petstagram.models import Profile, PetPhoto, Pet


def show_profile(request):
    profile = get_profile()
    pets = Pet.objects.filter(user_profile=profile)
    pet_photos = PetPhoto.objects.filter(tagged_pets__user_profile=profile).distinct()
    total_likes_count = sum(pp.likes for pp in pet_photos)
    total_images_count = len(pet_photos)
    context = {
        'profile': get_profile(),
        'images': total_images_count,
        'likes': total_likes_count,
        'pets': pets
    }
    return render(request, 'profile_details.html', context)


def profile_action(request, form_class, template_name, url, instance):
    if request.method == "POST":
        form = form_class(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(url)
    else:
        form = form_class(instance=instance)

    context = {
        'form': form
    }

    return render(request, template_name, context)


def create_profile(request):
    if request.method == "POST":
        profile_form = ProfileForm(request.POST)
        if profile_form.is_valid():
            profile = Profile(**profile_form.cleaned_data)
            profile.save()
            return redirect('home')
    else:
        profile_form = ProfileForm()
        context = {
            'form': profile_form
        }
        return render(request, 'part2/profile_create.html', context)


def edit_profile(request):
    profile = get_profile()
    if request.method == "POST":
        profile_form = ProfileEditForm(request.POST, instance=profile, initial={'gender': profile.DO_NOT_ASK})
        if profile_form.is_valid():
            profile_form.save()

    else:
        profile_form = ProfileEditForm(instance=profile, initial={'gender': profile.DO_NOT_ASK})

    context = {
        'profile_form': profile_form,
    }
    return render(request, 'part2/profile_edit.html', context)


def delete_profile(request):
    if request.method == "POST":
        profile = get_profile()
        pets = Pet.objects.filter(user_profile=profile)
        pet_photos = PetPhoto.objects.filter(tagged_pets__user_profile=profile).delete()
        profile.delete()
        pets.delete()

        return redirect('home')
    context = {}
    return render(request, 'part2/profile_delete.html', context)

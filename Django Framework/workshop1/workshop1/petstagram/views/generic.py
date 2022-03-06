from django.shortcuts import render

from workshop1.petstagram.helpers import get_profile
from workshop1.petstagram.models import PetPhoto


def show_home(request):
    context = {
        'hide_additional_buttons': True
    }

    return render(request, 'home_page.html', context)


def show_dashboard(request):
    profile = get_profile()
    pets = profile.pet_set.all()
    context = {
        'has_photos': False,
        'profile': profile,
        'pets': pets,
    }

    all_photos = PetPhoto.objects.prefetch_related('tagged_pets').filter(tagged_pets__user_profile=profile.id)
    if all_photos.exists():
        context['has_photos'] = True
        context['pet_photos'] = all_photos

    return render(request, 'dashboard.html', context)

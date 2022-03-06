from django.shortcuts import render, redirect

from workshop1.petstagram.forms.forms import PetForm, EditPetForm, DeletePetForm
from workshop1.petstagram.helpers import get_profile
from workshop1.petstagram.models import Pet


def pet_action(request, form_class, url, instance, template_name):
    if request.method == "POST":
        form = form_class(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(url)
    else:
        form = form_class(instance=instance)

    context = {
        'form': form,
        'pet': instance
    }

    return render(request, template_name, context)


def add_pet(request):
    profile = get_profile()

    return pet_action(request, PetForm, 'profile', Pet(user_profile=profile), 'part2/pet_create.html')


def edit_pet(request, pk):
    return pet_action(request, EditPetForm, 'profile', Pet.objects.get(pk=pk), 'part2/pet_edit.html')


def delete_pet(request, pk):
    return pet_action(request, DeletePetForm, 'profile', Pet.objects.get(pk=pk), 'part2/pet_delete.html')

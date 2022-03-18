from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views
from ws_exercise.petstagram.forms import ProfileCreateForm, AddPetForm, AddPhotoForm, ProfileEditForm, DeleteForm, \
    PetEditForm, PetDeleteForm, EditPhoto
from ws_exercise.petstagram.models import Profile, PetPhoto, Pet

UserModel = get_user_model()


class HomeView(views.TemplateView):
    def get_template_names(self):
        if self.request.user.is_authenticated:
            return 'dashboard.html'
        else:
            return 'auth_pages/home_page.html'

    # def dispatch(self, request, *args, **kwargs):
    #     if self.request.user.is_authenticated:
    #         return

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        result['in_home'] = True


def show_dashboard(request):
    profile = UserModel
    # pet_photos = PetPhoto.objects.filter(tagged_pets__user=profile).distinct()
    #
    # context = {
    #
    #     'pet_photos': pet_photos,
    #
    # }

    return render(request, 'dashboard.html')


def show_profile(request):
    profile = get_profile()
    pets = Pet.objects.filter(user=profile)
    total_img = PetPhoto.objects.filter(tagged_pets__user=profile).distinct()
    total_img_count = total_img.count()
    total_likes = sum(x.likes for x in total_img)

    context = {
        'profile': profile,
        'pets': pets,
        'count': total_img_count,
        'likes': total_likes,
    }

    return render(request, 'profile_details.html', context)


def show_photo_details(request, id):
    photo = PetPhoto.objects.all().get(id=id)

    context = {
        'photo': photo
    }

    return render(request, 'photo_details.html', context)


def photo_like(request, id):
    photo = PetPhoto.objects.get(id=id)
    photo.likes += 1
    photo.save()
    return redirect('photo_details', photo.pk)


def create_profile(request):
    if request.method == "POST":
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = ProfileCreateForm()

    context = {
        'form': form
    }

    return render(request, 'part2/profile_create.html', context)


def edit_profile(request):
    profile = get_profile()
    if request.method == "POST":
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')

    else:
        form = ProfileEditForm(instance=profile)

    context = {
        'form': form
    }

    return render(request, 'part2/profile_edit.html', context)


def delete_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        delete_form = DeleteForm(request.POST, instance=profile)
        if delete_form.is_valid():
            delete_form.save()
            return redirect('home')
    else:
        delete_form = DeleteForm()

    context = {
        'delete_form': delete_form
    }
    return render(request, 'part2/profile_delete.html', context)


def add_pet(request):
    profile = get_profile()
    pet = Pet(user=profile)
    if request.method == "POST":
        form = AddPetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddPetForm(instance=pet)

    context = {
        'form': form
    }
    return render(request, 'part2/pet_create.html', context)


def edit_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'POST':
        form = PetEditForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = PetEditForm(instance=pet)

    context = {'form': form,
               'pet': pet}
    return render(request, 'part2/pet_edit.html', context)


def delete_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'POST':
        form = PetDeleteForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = PetDeleteForm(instance=pet)

    context = {'form': form,
               'pet': pet}
    return render(request, 'part2/pet_delete.html', context)


def add_photo(request):
    if request.method == "POST":
        form = AddPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = AddPhotoForm()

    context = {
        'form': form
    }

    return render(request, 'part2/photo_create.html', context)


def edit_photo(request, pk):
    photo = PetPhoto.objects.get(pk=pk)
    if request.method == "POST":
        form = EditPhoto(request.POST, instance=photo)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = EditPhoto(instance=photo)

    context = {
        'form': form,
        'photo': photo
    }

    return render(request, 'part2/photo_edit.html', context)

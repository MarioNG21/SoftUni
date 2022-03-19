from django.contrib.auth import get_user_model
from django.contrib.auth import mixins as auth_mixins
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views
from ws_exercise.petstagram.forms import ProfileCreateForm, AddPetForm, AddPhotoForm, ProfileEditForm, DeleteForm, \
    PetEditForm, PetDeleteForm, EditPhoto
from ws_exercise.petstagram.models import Profile, PetPhoto, Pet

UserModel = get_user_model()


class HomeView(views.TemplateView):

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(reverse_lazy('dashboard'))
        return redirect(reverse_lazy('home'))

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        result['in_home'] = True


class DashboardView(views.ListView):
    template_name = 'dashboard.html'
    model = PetPhoto
    context_object_name = 'pet_photos'


class ProfileView(views.DetailView):
    model = Profile
    template_name = 'profile_details.html'

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs['pk'] = self.request.user.id
        kwargs['pets'] = Pet.objects.filter(user=self.request.user)
        kwargs['count'] = PetPhoto.objects.filter(user=self.request.user).distinct().count()
        kwargs['likes'] = sum(x.likes for x in PetPhoto.objects.filter(user=self.request.user).distinct())
        return kwargs

    def get_queryset(self):
        queryset = super().get_queryset()
        result = queryset.filter(pk=self.request.user.pk)
        return result


#
# def show_profile(request):
#     profile = get_profile()
#     pets = Pet.objects.filter(user=profile)
#     total_img = PetPhoto.objects.filter(tagged_pets__user=profile).distinct()
#     total_img_count = total_img.count()
#     total_likes = sum(x.likes for x in total_img)
#
#     context = {
#         'profile': profile,
#         'pets': pets,
#         'count': total_img_count,
#         'likes': total_likes,
#     }
#
#     return render(request, 'profile_details.html', context)


class PetPhotoDetails(views.DetailView):
    model = PetPhoto
    template_name = 'photo_details.html'
    context_object_name = 'photo'

    def get_queryset(self):
        return super().get_queryset().prefetch_related('tagged_pets')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['owner'] = False
        if self.request.user == self.object.user:
            context['owner'] = True

        return context


def photo_like(request, pk):
    photo = PetPhoto.objects.get(pk=pk)
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


class CreatePetView(views.CreateView, auth_mixins.LoginRequiredMixin):
    template_name = 'part2/pet_create.html'
    form_class = AddPetForm

    success_url = reverse_lazy('home')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class EditPetView(views.UpdateView):
    model = Pet
    template_name = 'dashboard.html'
    success_url = reverse_lazy('profile')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class DeletePetView(views.DeleteView):
    template_name = 'part2/pet_delete.html'
    model = Pet
    success_url = reverse_lazy('profile')
    context_object_name = 'pet'

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class AddPhotoView(views.CreateView):
    form_class = AddPhotoForm
    template_name = 'part2/photo_create.html'
    success_url = reverse_lazy('dashboard')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class EditPhotoView(views.UpdateView):
    form_class = EditPhoto
    template_name = 'part2/photo_edit.html'
    success_url = reverse_lazy('dashboard')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

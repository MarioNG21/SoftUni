from django.contrib.auth import views as auth_views, get_user_model
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.views.generic import detail
from django.urls import reverse_lazy, reverse
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins
from My_final_social_media_shop.auth_acc.forms import CreationUser, ForgotPasswordForm, ProfileUpdateForm, \
    CreateProfileForm
from My_final_social_media_shop.auth_acc.models import Profile, AppUser


UserModel = get_user_model()


class UserRegistrationView(views.CreateView):
    form_class = CreationUser
    template_name = 'auth/registration.html'
    success_url = reverse_lazy('login user')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()

    def form_valid(self, form):
        result = super().form_valid(form)
        if self.request.method == 'POST':
            profile = Profile.objects.create(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                age=form.cleaned_data['age'],
                gender=form.cleaned_data['gender'],
                user=form.instance,
            )
            profile.save()

            # Sending Email
            current_domain = get_current_site(self.request)
            email_subject = 'User Activation Link'
            context = {
                'user': form.instance,
                'domain': current_domain,
                'uid': urlsafe_base64_encode(force_bytes(form.instance.pk)),
                'token': default_token_generator.make_token(form.instance)
            }

            message = render_to_string('auth/email.html', context)
            to_email = form.instance.email
            send_email = EmailMessage(email_subject, message, to=[to_email])
            send_email.send()

            result.headers['Location'] = reverse_lazy(
                'login user') + f'?command=verification&email={form.instance.email}'

        return result


class UserLoginView(auth_views.LoginView):
    template_name = 'auth/login.html'
    model = UserModel
    success_url = reverse_lazy('index')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class UserLogoutView(auth_mixins.LoginRequiredMixin, auth_views.LogoutView):
    template_name = 'auth/logout.html'
    next_page = reverse_lazy('index')


class UserChangePasswordView(auth_views.PasswordResetConfirmView):
    template_name = 'auth/change_password.html'
    form_class = PasswordChangeForm
    success_url = reverse_lazy('login user')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['uidb64'] = self.kwargs['uidb64']
        context['token'] = self.kwargs['token']
        return context


class ForgotPasswordsView(views.FormView):
    template_name = 'auth/forgot_pass_view.html'
    form_class = ForgotPasswordForm
    success_url = reverse_lazy('login user')

    def form_valid(self, form):
        result = super().form_valid(form)
        if self.request.method == "POST":
            '''
            todo: 
                ---- make function sending this meals to look something like this send_mail(request, user, template_to_render, email, command) ----
            
            '''
            user = AppUser.objects.get(email=form.cleaned_data['email'])
            current_domain = get_current_site(self.request)
            email_subject = 'Password Reset Link'
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            context = {
                'user': user,
                'domain': current_domain,
                'uid': uid,
                'token': token
            }

            message = render_to_string('auth/forgot_passwords.html', context)
            to_email = form.cleaned_data['email']
            send_email = EmailMessage(email_subject, message, to=[to_email])
            send_email.send()

            result.headers['Location'] = reverse_lazy(
                'login user') + f'?command=resetpassword&email={form.cleaned_data["email"]}'

        return result


class ActivationView(detail.BaseDetailView):
    def get(self, request, *args, **kwargs):
        try:
            uid = kwargs.get('uid')
            decoded_uid = urlsafe_base64_decode(uid).decode()
            user = AppUser.objects.get(pk=decoded_uid)

        except(TypeError, ValueError, OverflowError, AppUser.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, kwargs.get('token')):
            user.is_active = True
            user.save()

        else:
            return redirect('register user')

        return redirect('login user')


class CreateProfileView(views.CreateView):
    template_name = 'auth/create_profile.html'
    success_url = reverse_lazy('index')
    form_class = CreateProfileForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class UpdateProfileView(views.UpdateView):
    template_name = 'auth/profile_update.html'
    form_class = ProfileUpdateForm
    success_url = reverse_lazy('index')
    model = Profile

    def get_success_url(self):
        if self.success_url:
            return self.success_url

        return super().get_success_url()


class DeleteProfileView(views.DeleteView):
    template_name = 'auth/profile_delete.html'
    success_url = reverse_lazy('index')
    model = Profile




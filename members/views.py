from re import template
from blog.models import Profile
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.views.generic import DetailView, CreateView
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm, PasswordChangingForm, ProfilePageForm
from django.contrib.auth.views import PasswordChangeView

#------------------------------------------------------------------------------------------------------------------------------------------------------

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

#------------------------------------------------------------------------------------------------------------------------------------------------------

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('bloghome')

    def get_object(self):
        return self.request.user

#------------------------------------------------------------------------------------------------------------------------------------------------------

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_success')

def password_success(request):
    return render(request, 'registration/password_success.html', {})

#------------------------------------------------------------------------------------------------------------------------------------------------------

class ProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context

#------------------------------------------------------------------------------------------------------------------------------------------------------

class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    fields = [
        'bio', 'profile_pic',
        'website_url', 'instagram_url',
        'facebook_url', 'twitter_url', 
        'linkedin_url', 'snapchat_url',
        ]
    success_url = reverse_lazy('bloghome')

#------------------------------------------------------------------------------------------------------------------------------------------------------

class CreateProfilePageView(CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/Create_user_profile_page.html'
    #fields = '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
from django.shortcuts import render
from django.views import generic

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
# from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import redirect
from .forms import SignUpForm, EditProfileForm

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    
    

class UserEditView(generic.UpdateView):
    form_class =  EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')
    
    def get_object(self):
        return self.request.user
    
# class PasswordsChangeView(PasswordChangeView):
#     form_class = PasswordChangingForm
#     # form_class = PasswordChangeForm
#     success_url = reverse_lazy('password_success')
#     # success_url = reverse_lazy('home')

# def password_success(request):
#     return render(request, 'registration/password_success.html', {})

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
# Create your views here.


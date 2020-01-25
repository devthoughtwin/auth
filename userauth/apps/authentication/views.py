from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.views.generic import ListView, UpdateView, DetailView, CreateView, FormView, TemplateView, RedirectView
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from authentication.forms import RegistrationForm, UserProfileForm
from django.urls import reverse
from authentication.models import UserProfile
from django.contrib.auth import get_user_model

User = get_user_model()

class SignUpView(FormView):
    form_class = RegistrationForm
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        user = form.save(False)
        user.set_password(form.cleaned_data.get('password1'))
        user.is_active = True
        user.save()

        user = authenticate(username=user.username, password=form.data['password1'])
        login(self.request, user)
        return HttpResponseRedirect(reverse('authentication:home'))

# class LoginView(FormView):
#     form_class = AuthenticationForm
#     template_name = 'registration/login.html'

#     def form_valid(self, form):
#         username = form.cleaned_data.get('username')
#         password = form.cleaned_data.get('password')
#         user = authenticate(username=username, password=password)
#         login(self.request, user)
#         return redirect('home')

# class LogoutView(RedirectView):
#     """
#     Provides users the ability to logout
#     """
#     url = '/home/'

#     def get(self, request, *args, **kwargs):
#         logout(request)
#         return super(LogoutView, self).get(request, *args, **kwargs)

class ProfileView(LoginRequiredMixin, View):
    login_url = '/accounts/login/'

    def get(self, request):

        return render(request, 'registration/profile.html')


class EditUserProfileView(LoginRequiredMixin, UpdateView): #Note that we are using UpdateView and not FormView
    model = UserProfile
    form_class = UserProfileForm
    template_name = "registration/profile.html"

    def get_object(self, *args, **kwargs):

        user = get_object_or_404(User, pk=self.request.user.pk)

        # We can also get user object using self.request.user  but that doesnt work
        # for other models.

        return user.profile

    def get_success_url(self, *args, **kwargs):
        return reverse("authentication:profile")


class HomeView(TemplateView):
    template_name = 'deshboard.html'
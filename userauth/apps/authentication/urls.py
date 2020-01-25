from django.urls import path
from authentication.views import SignUpView, ProfileView, HomeView, EditUserProfileView
from django.contrib.auth.views import LoginView, LogoutView

app_name='authentication'

urlpatterns = [
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('accounts/profile/', EditUserProfileView.as_view(), name='profile'),
    path('home/', HomeView.as_view(), name='home')
]
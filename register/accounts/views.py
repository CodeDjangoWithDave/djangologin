from django.shortcuts import render
from .forms import UserLoginForm
# Create your views here.

from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView



# Custom login view
class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    form_class = UserLoginForm

# Custom logout view
class CustomLogoutView(LogoutView):
    template_name = 'accounts/logout.html'

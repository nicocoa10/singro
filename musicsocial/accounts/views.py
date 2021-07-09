from django.shortcuts import render
from django.urls import reverse_lazy
# Create your views here.
from . import forms

from django.views.generic import CreateView


class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login') # once someone has signed up to our website we will reverse them to the login page WHEN they click singup
    template_name = 'accounts/signup.html'

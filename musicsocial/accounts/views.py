from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic.base import View
from django.views.generic.detail import DetailView
# Create your views here.
from . import forms

from django.views.generic import CreateView


class ShowProfilePageView(LoginRequiredMixin, DetailView):

    model = get_user_model()
    template_name = 'accounts/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ShowProfilePageView,
                        self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(get_user_model(), id=self.kwargs['pk'])

        context['page_user'] = page_user
        return context


class SignUp(CreateView):
    form_class = forms.UserCreateForm
    # once someone has signed up to our website we will reverse them to the login page WHEN they click singup
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

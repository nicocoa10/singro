from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.urls import reverse
from django.views import generic
from django.contrib import messages
from groups.models import Group, GroupMember


# Create your views here.

class CreateGroup(LoginRequiredMixin, generic.CreateView):

    fields = ('name', 'description')

    model = Group


class SingleGroup(generic.DetailView):
    model = Group


class LisGroup(generic.ListView):
    model = Group


class JoinGroup(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:single', kwargs={'slug': self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):
        group = get_object_or_404(Group, slug=self.kwargs.get('slug'))

        try:
            GroupMember.objects.create(user=self.request.user, group=group)

        except:
            messages.warning(self.request, 'warning already a member!')
        else:
            messages.success(self.request, 'You are now a member!')

        return super().get(request, *args, **kwargs)


class LeaveGroup(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:single', kwargs={'slug': self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):

        try:
            membership = GroupMember.objects.filter(

                user=self.request.user,
                group__slug=self.kwargs.get('slug')

            ).get()

        except GroupMember.DoesNotExist:
            messages.warning(self.request, 'Sorry You arent in this Group!!')
        else:
            membership.delete()
            messages.success(self.request, 'You have left the group!')

        return super().get(request, *args, **kwargs)

    pass

from django.contrib import admin
from groups.models import Group
from . import models
# Register your models here.


class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember

admin.site.register(models.Group)
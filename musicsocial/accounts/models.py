from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from django.contrib import auth
# Create your models here.


class NewUser(AbstractUser):

    first_name = models.CharField(max_length=150, unique=False)
    about = models.TextField(_('about'), max_length=500, blank=True)
    favorite_genre = models.CharField(max_length=150)
    music_link = models.URLField(max_length=200)
    profile_pic = models.ImageField(upload_to='user_images_raw', blank=True)

    def __str__(self):
        return '@{}'.format(self.username)

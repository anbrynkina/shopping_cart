from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    # can add an opportunity to load picture
    image = models.ImageField(upload_to='users_images', blank=True)
    # after trying to migrate we may have a conflict because User model was already added by Django
    # to resolve this we need to delete our BD and use fixtures to restore it
    # for future projects it would be better to create User first

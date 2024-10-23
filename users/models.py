from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """
    Create instance of default user model to
    allow for easy changes if needed later
    """

    # Custom related_name to prevent conflict
    groups = models.ManyToManyField(
        'auth.Group', related_name='customuser_set',
        blank=True, help_text='The groups this user belongs to.',
        verbose_name='groups')

    user_permissions = models.ManyToManyField(
        'auth.Permission', blank=True,
        related_name='customuser_permissions',
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
        )


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name='profile')

    bio = models.TextField(blank=True, null=True)
    profile_pic = models.ImageField(
        upload_to="profiles/", blank=True, null=True)

    location = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s profile"

from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(to='auth.User',
                                on_delete=models.CASCADE,
                                related_name='profile')

    @classmethod
    def generate_profile(cls):
        for user in User.objects.all():
            try:
                user.profile
            except ValueError:
                profile = Profile()
                profile.user = user
                profile.save()

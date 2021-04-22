from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    phone = models.IntegerField(default=0)

    def create_profile(sender, **kwargs):
        if kwargs['created']:
            user_profile = UserProfile.objects.create(user=kwargs['instance'])

    post_save.connect(create_profile, sender=User)


# Based on Youtube vid: https://www.youtube.com/watch?v=mWNeTTDB3zQ&list=PLw02n0FEB3E3VSHjyYMcFadtQORvl1Ssj&index=11
# Creating a user specific model / database for users to store their inventory items.
class UserInventory(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    item = models.CharField(max_length=100, default='')
    description = models.TextField(max_length=100, default='')
    location = models.CharField(max_length=100, default=100)
    image = models.CharField(max_length=100)


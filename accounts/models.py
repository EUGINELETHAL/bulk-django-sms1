from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=30, blank=True)
    institution = models.CharField(max_length=255)
    created = models.DateField(auto_now_add=True)
    email_confirmed = models.BooleanField(default=False)
    africastalking_api_key = models.CharField(max_length=256, null=True, blank=True)
    africastalking_username = models.CharField(max_length=128, null=True, blank=True)
    africastalking_sender_id = models.CharField(max_length=128, null=True, blank=True)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

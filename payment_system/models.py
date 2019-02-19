from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField
import datetime as dt
import string as str
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.CharField(max_length=30, blank=True)
    email = models.EmailField()
    phone_number = PhoneNumberField(max_length=10, blank=True)
    location = models.CharField(max_length=30, blank=True)


    User.profile = property(lambda u: Profile.objects.get_or_create(user=u)[0])

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:

        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):

    instance.profile.save()

@classmethod
def get_profile(cls,user_id):
    profiles = Profile.objects.all()
    other_userprofiles = []
    for profile in profiles:
        if profile.user_id !=user_id:
             other_userprofiles.append(profile)
    return other_userprofiles


def generate_id():
        n = 10
        random = str.ascii_uppercase + str.ascii_lowercase + str.digits
        return ''.join(choice(random) for _ in range(n))




# end
# class Profile(models.Model):
#     name = models.CharField(max_length=120)
#     description = models.TextField(default='description default text')
#
#     def __str__(self):
#         return self.name
#
#     def save_profile(self):
#         self.save()
#
#     @classmethod
#     def get_profile(cls):
#         profile = Profile.objects.all()
#
#         return profile
#
#     class Meta:
#         ordering = ['name']

class ContactRecipient(models.Model):
    full_name = models.CharField(max_length = 30)
    email = models.EmailField()
    comment = models.TextField()

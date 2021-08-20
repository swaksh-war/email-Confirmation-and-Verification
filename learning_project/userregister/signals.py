from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from . models import Profile

#it will make sure about the functions working like it will create profile in this case
@receiver(post_save, sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

#it will save profile infos and it will make a profile in Django Server
@receiver(post_save, sender=User)
def save_profile(sender,instance,created,**kwargs):
    if created:
        instance.profile.save()
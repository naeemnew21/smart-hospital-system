from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from random import choice
from string import ascii_lowercase, digits

from xstaff.models import JobProfile
from .models import MyUser, UserProfile, UserVital
from .validme import ID_Valid



def generate_random_username(length=16, chars=ascii_lowercase+digits, split=4, delimiter='-'):
    username = ''.join([choice(chars) for i in range(length)])
    if split:
        username = delimiter.join([username[start:start+split] for start in range(0, len(username), split)])
    try:
        MyUser.objects.get(username=username)
        return generate_random_username(length=length, chars=chars, split=split, delimiter=delimiter)
    except MyUser.DoesNotExist:
        return username




@receiver(pre_save, sender=MyUser)
def my_callback(sender, instance, *args, **kwargs):
    #if not(instance.username):
    instance.username = generate_random_username()




@receiver(post_save, sender=MyUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(
            user=instance,
            birth_date = ID_Valid(instance.national_id).get_birth(), # year-month-day
            sex = ID_Valid(instance.national_id).get_sex() # Male/Female
            )
        UserVital.objects.create(user=instance)
        if instance.is_staff and not(instance.is_superuser):
            JobProfile.objects.create(user = instance)
        if instance.is_superuser:
            JobProfile.objects.create(user = instance, job='HR')
            instance.is_superuser = False
            instance.save()



@receiver(post_save, sender=MyUser)
def save_user_profile(sender, instance, **kwargs):
    exist = JobProfile.objects.filter(user=instance).exists()
    if not(exist) and instance.is_staff:
        JobProfile.objects.create(user=instance)
 

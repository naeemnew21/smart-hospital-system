from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from xstaff_secretary.models import Secretary
from .models import JobProfile
from xstaff_doctor.models import Doctor




@receiver(post_save, sender=JobProfile)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.job == 'Dr':
            Doctor.objects.create(user = instance.user)
        if instance.job == 'Secretary':
            Secretary.objects.create(user = instance.user)




@receiver(post_save, sender=JobProfile)
def save_user_profile(sender, instance, **kwargs):
    if instance.job == 'Dr':
        exist = Doctor.objects.filter(user=instance.user).exists()
        if not(exist):
            Doctor.objects.create(user=instance.user)
            
    if instance.job == 'Secretary':
        exist = Secretary.objects.filter(user=instance.user).exists()
        if not(exist):
            Secretary.objects.create(user=instance.user)
    
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from .models import Prescription, RequestPrescription




@receiver(post_save, sender=Prescription)
def create_request_pre(sender, instance, created, **kwargs):
    if created:
        RequestPrescription.objects.create(model = instance)



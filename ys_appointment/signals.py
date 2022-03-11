from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from .models import AppointModel, RequsetAppointment




@receiver(post_save, sender=AppointModel)
def create_request_app(sender, instance, created, **kwargs):
    if created:
        RequsetAppointment.objects.create(model = instance)



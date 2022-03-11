from django.apps import AppConfig


class YsAppointmentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ys_appointment'
    
    def ready(self):
        from . import signals

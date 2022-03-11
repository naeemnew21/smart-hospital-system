from django.contrib import admin
from .models import Pharmacy, Medicine, Prescription, RequestPrescription

admin.site.register(Pharmacy)
admin.site.register(Medicine)
admin.site.register(Prescription)
admin.site.register(RequestPrescription)
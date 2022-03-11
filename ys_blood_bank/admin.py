from django.contrib import admin
from .models import Bloodbank, BloodModel, RequestBlood

admin.site.register(Bloodbank)
admin.site.register(BloodModel)
admin.site.register(RequestBlood)

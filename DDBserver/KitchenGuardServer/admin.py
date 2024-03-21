from django.contrib import admin
from .models import Sensor
from .models import Patient
from .models import Event

admin.site.register(Sensor)
admin.site.register(Patient)
admin.site.register(Event)

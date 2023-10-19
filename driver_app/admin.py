from django.contrib import admin

from .models import Driver, DriverType
admin.site.register(Driver)
admin.site.register(DriverType)
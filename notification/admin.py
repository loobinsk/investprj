from django.contrib import admin
from .models import Notification, Signal


admin.site.register(Notification)
admin.site.register(Signal)
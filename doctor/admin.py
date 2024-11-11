from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .models import Doctor
from .models import Notification

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('user','image','full_name','mobile','country','bio_data','specialization','qualification',)
   

admin.site.register(Doctor, DoctorAdmin)

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'type','seen',)
   

admin.site.register(Notification, NotificationAdmin)


from django.contrib import admin

# Register your models here.
from .models import Patient
from .models import Notification

class PatientAdmin(admin.ModelAdmin):
    # list_display = ('user','image','full_name','mobile','country','bio_data','specialization','qualification',)
   pass

admin.site.register(Patient, PatientAdmin)

class NotificationAdmin(admin.ModelAdmin):
    # list_display = ('doctor', 'type','seen',)
  pass 

admin.site.register(Notification, NotificationAdmin)

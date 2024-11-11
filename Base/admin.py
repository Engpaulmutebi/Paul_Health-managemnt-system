from django.contrib import admin
from Base import models

class AppointmentInline(admin.TabularInline):
  models = models.Appointment
  extra = 1

class MedicalRecordInline(admin.TabularInline):
  models = models.MedicalRecord
  extra = 1

class LabTestInline(admin.TabularInline):
  models = models.LabTest
  extra = 1

class PrescriptionInline(admin.TabularInline):
  models = models.Prescription
  extra = 1

class BillingInline(admin.TabularInline):
  models = models.Billing
  extra = 1

class ServiceAdmin(admin.ModelAdmin):
  list_display = ['name','cost']
  search_fields = ['name','description']
  filter_horizontal = ['available_doctors']

class AppointmentAdmin(admin.ModelAdmin):
  list_display = ['patient','doctor','appointment_date','status']
  search_fields = ['patient__username','doctor__user__username']
  inline = [MedicalRecordInline,LabTestInline,PrescriptionInline,BillingInline]

class MedicalRecordAdmin(admin.ModelAdmin):
  list_display = ['appointment','diagnosis']
  

class LabTestAdmin(admin.ModelAdmin):
  list_display = ['appointment','test_name'] 

class PrescriptionAdmin(admin.ModelAdmin):
  list_display = ['appointment','medication'] 

class BillingAdmin(admin.ModelAdmin):
  list_display = ['patient','total','status','date'] 


admin.site.register(models.Service, ServiceAdmin)
admin.site.register(models.Appointment, AppointmentAdmin)
admin.site.register(models.Billing, BillingAdmin)
admin.site.register(models.LabTest, LabTestAdmin)
admin.site.register(models.Prescription, PrescriptionAdmin)
admin.site.register(models.MedicalRecord, MedicalRecordAdmin)
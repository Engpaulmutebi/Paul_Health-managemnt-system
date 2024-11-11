from django.db import models

from userauths import models as userauths_model
from django.utils import timezone


class Patient(models.Model):
  user = models.OneToOneField(userauths_model.User,on_delete = models.CASCADE)
  image = models.FileField(upload_to= "images",null=True,blank=True)
  full_name = models.CharField(max_length=100, null=True, blank=True)
  mobile = models.CharField(max_length=100, null=True, blank=True)
  gender = models.CharField(max_length=100, null=True, blank=True)
  blood_group = models.CharField(max_length=100, null=True, blank=True)
  email= models.CharField(max_length=100, null=True, blank=True)
  address= models.CharField(max_length=100, null=True, blank=True)
  email = models.CharField(max_length=100, null=True, blank=True)
  

  def __str__(self):
    return self.full_name
  
class Notification(models.Model):

  NOTIFICATION_TYPE = (
    ('Appointment_Scheduled','Appointment_Scheduled'),
    ('Appointment_Cancelled','Appointment_Cancelled')
  ) 
  patient = models.ForeignKey(Patient, on_delete=models.SET_NULL,null=True,blank=True)

  appointment = models.ForeignKey('Base.Appointment', on_delete=models.CASCADE,null=True,blank=True,related_name='patient_appointment_Notification') 

  type = models.CharField(max_length=100, choices=NOTIFICATION_TYPE)
  seen = models.DateField(auto_now_add=True)
   
  class Meta:
    verbose_name_plural = "Notification" 

  def __str__(self) -> str:
    return f"DR.{self.patient.full_name} Notification"





